"""
Story Generation Module
Uses Claude AI to generate pedagogically appropriate leveled readers
"""

import os
from anthropic import Anthropic
from reading_levels import get_writing_guidelines


class StoryGenerator:
    def __init__(self, api_key=None):
        """Initialize the story generator with Anthropic API"""
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY must be set in environment or passed as parameter")
        self.client = Anthropic(api_key=self.api_key)

    def generate_story(self, reading_level, characters, story_prompts=None, theme=None):
        """
        Generate a leveled reader story based on inputs

        Args:
            reading_level: Target reading level (e.g., "Kindergarten", "2nd Grade")
            characters: List of dicts with 'name' and 'gender' keys
            story_prompts: Optional dict with story direction questions
            theme: Optional theme for the story

        Returns:
            dict with 'title', 'pages' (list of page content), 'scene_descriptions'
        """
        guidelines = get_writing_guidelines(reading_level)
        if not guidelines:
            raise ValueError(f"Invalid reading level: {reading_level}")

        # Build character descriptions
        char_descriptions = []
        for i, char in enumerate(characters):
            name = char.get('name', f'Character{i+1}')
            gender = char.get('gender', 'non-binary')

            # Build detailed character description
            desc_parts = [f"{name} ({gender})"]

            # Add physical appearance details if provided
            appearance = []
            if char.get('age'):
                appearance.append(f"{char['age']}")
            if char.get('skin_tone'):
                appearance.append(f"{char['skin_tone']} skin")
            if char.get('hair_color'):
                appearance.append(f"{char['hair_color']} hair")
            if char.get('eye_color'):
                appearance.append(f"{char['eye_color']} eyes")
            if char.get('other_features'):
                appearance.append(f"{char['other_features']}")
            if char.get('clothing'):
                appearance.append(f"wearing {char['clothing']}")

            if appearance:
                desc_parts.append(": " + ", ".join(appearance))

            char_descriptions.append(f"- {''.join(desc_parts)}")

        # Build story prompts section
        prompt_section = ""
        if story_prompts and any(story_prompts.values()):
            prompt_section = "\n\nStory Direction (incorporate these elements if provided):\n"
            for key, value in story_prompts.items():
                if value:
                    prompt_section += f"- {key}: {value}\n"

        # Build the comprehensive prompt for Claude
        system_prompt = f"""You are an expert educational content creator specializing in leveled readers for children.
You create stories that are pedagogically sound, engaging, and appropriate for specific reading levels.

You must follow these strict guidelines for {reading_level} level:

READING LEVEL SPECIFICATIONS:
- Guided Reading Level: {guidelines['guided_reading_level']}
- Grade Equivalent: {guidelines['grade']}
- Lexile Level: {guidelines['lexile']}

WRITING CONSTRAINTS:
- Words per page: {guidelines['words_per_page']}
- Sentence style: {guidelines['sentence_style']}
- Vocabulary: {guidelines['vocabulary_level']}
- Concepts: {guidelines['concept_complexity']}

PEDAGOGICAL REQUIREMENTS:
- Focus: {guidelines['pedagogical_focus']}
- Support features: {guidelines['support_features']}

STORY REQUIREMENTS:
1. Create an engaging story appropriate for the reading level
2. Use the provided characters naturally in the story
3. Ensure vocabulary and sentence structure match the level precisely
4. Create a clear narrative structure (beginning, middle, end)
5. Include age-appropriate themes and concepts
6. Make the story educational yet entertaining
7. Each page should be suitable for illustration

OUTPUT FORMAT:
CRITICAL: You must return ONLY valid JSON. No extra text before or after.

Provide your response as a structured JSON object with this EXACT format:
{{
    "title": "Story Title Here",
    "pages": [
        {{
            "page_number": 1,
            "text": "The text that appears on this page",
            "scene_description": "Detailed description of what should be illustrated on this page, including character appearance, setting, actions, and mood"
        }}
    ],
    "character_descriptions": {{
        "CharacterName": "Detailed consistent description of character appearance for illustrations"
    }}
}}

IMPORTANT JSON RULES:
- Use double quotes for all strings, never single quotes
- No trailing commas after the last item in arrays or objects
- Escape any quotes within text with backslash
- Ensure all brackets and braces are properly closed
- Return ONLY the JSON object, nothing else
"""

        user_prompt = f"""Create a leveled reader story for {reading_level} with the following specifications:

CHARACTERS:
{chr(10).join(char_descriptions)}

THEME: {theme or 'Create an age-appropriate theme'}
{prompt_section}

Remember to:
1. Strictly adhere to the reading level guidelines
2. Create 6-10 pages depending on the reading level
3. Make each page suitable for a single illustration
4. Ensure the story has educational value
5. Keep vocabulary and sentence structure appropriate
6. Provide detailed scene descriptions for consistent illustrations
7. Provide consistent character descriptions for the illustrator

Generate the story now in the specified JSON format."""

        try:
            response = self.client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=4000,
                temperature=0.7,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_prompt}
                ]
            )

            # Extract the text content
            content = response.content[0].text

            # Try to parse as JSON
            import json
            import re

            # Find JSON in the response (it might be wrapped in markdown code blocks)
            original_content = content
            if "```json" in content:
                json_start = content.find("```json") + 7
                json_end = content.find("```", json_start)
                content = content[json_start:json_end].strip()
            elif "```" in content:
                json_start = content.find("```") + 3
                json_end = content.find("```", json_start)
                content = content[json_start:json_end].strip()

            # Try to find JSON object if no code blocks
            if not content.strip().startswith("{"):
                # Look for the first { and last }
                match = re.search(r'\{.*\}', content, re.DOTALL)
                if match:
                    content = match.group(0)

            try:
                story_data = json.loads(content)
            except json.JSONDecodeError as json_err:
                # Log the problematic content for debugging
                print(f"JSON Parse Error: {json_err}")
                print(f"Attempted to parse: {content[:500]}...")

                # Try aggressive cleanup
                # 1. Remove trailing commas before closing brackets
                content = re.sub(r',(\s*[}\]])', r'\1', content)

                # 2. Fix common quote issues - replace smart quotes with regular quotes
                content = content.replace('"', '"').replace('"', '"')
                content = content.replace("'", "'").replace("'", "'")

                # 3. Try to fix unescaped quotes within strings (basic attempt)
                # This is tricky, but we can try to escape quotes that aren't part of JSON structure

                try:
                    story_data = json.loads(content)
                except json.JSONDecodeError as second_err:
                    print(f"Second JSON Parse Error: {second_err}")
                    print(f"Cleaned content: {content[:500]}...")

                    # Last resort: try to manually fix the JSON
                    # Remove any single quotes and replace with double quotes cautiously
                    # This is a heuristic and might not always work
                    raise ValueError(f"Could not parse JSON after cleanup attempts. Original error: {json_err}")

            return story_data

        except Exception as e:
            print(f"Error generating story: {e}")
            # Return a fallback structure
            return {
                "title": "Story Generation Error",
                "pages": [
                    {
                        "page_number": 1,
                        "text": f"Error generating story: {str(e)}",
                        "scene_description": "Error illustration"
                    }
                ],
                "character_descriptions": {}
            }

    def generate_story_variations(self, reading_level, characters, num_variations=3):
        """Generate multiple story variations for the same inputs"""
        variations = []
        for i in range(num_variations):
            story = self.generate_story(reading_level, characters)
            variations.append(story)
        return variations
