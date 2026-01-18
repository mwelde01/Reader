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
            char_descriptions.append(f"- {name} ({gender})")

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
Provide your response as a structured JSON object with:
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
        "CharacterName": "Detailed consistent description of character's appearance for illustrations"
    }}
}}
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
                model="claude-3-5-sonnet-20240620",
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
            # Find JSON in the response (it might be wrapped in markdown code blocks)
            if "```json" in content:
                json_start = content.find("```json") + 7
                json_end = content.find("```", json_start)
                content = content[json_start:json_end].strip()
            elif "```" in content:
                json_start = content.find("```") + 3
                json_end = content.find("```", json_start)
                content = content[json_start:json_end].strip()

            story_data = json.loads(content)
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
