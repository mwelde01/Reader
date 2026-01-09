"""
Image Generation Module
Generates consistent illustrations for leveled readers using AI
"""

import os
import base64
from io import BytesIO
from openai import OpenAI
from PIL import Image
import requests


class ImageGenerator:
    def __init__(self, api_key=None):
        """Initialize the image generator with OpenAI API"""
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY must be set in environment or passed as parameter")
        self.client = OpenAI(api_key=self.api_key)
        self.style_prompt = "children's book illustration style, colorful, friendly, educational, simple and clear composition, appropriate for young readers"

    def generate_page_illustration(self, scene_description, character_descriptions, page_number, art_style=None):
        """
        Generate an illustration for a specific page

        Args:
            scene_description: Description of what happens on this page
            character_descriptions: Dict of character names to appearance descriptions
            page_number: Page number for reference
            art_style: Optional specific art style (default: children's book illustration)

        Returns:
            PIL Image object
        """
        # Build comprehensive prompt with character consistency
        char_prompt = ""
        if character_descriptions:
            char_prompt = "\n\nCHARACTER APPEARANCES (maintain consistency):\n"
            for name, description in character_descriptions.items():
                char_prompt += f"- {name}: {description}\n"

        style = art_style or self.style_prompt

        full_prompt = f"""{scene_description}

{char_prompt}

Style: {style}

Important: This is page {page_number} of a children's reader. Keep characters consistent with their descriptions, use bright colors, clear compositions, and age-appropriate imagery."""

        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=full_prompt[:4000],  # DALL-E has prompt length limits
                size="1024x1024",
                quality="standard",
                n=1,
            )

            # Get the image URL and download it
            image_url = response.data[0].url
            image_response = requests.get(image_url)
            image = Image.open(BytesIO(image_response.content))

            return image

        except Exception as e:
            print(f"Error generating image for page {page_number}: {e}")
            # Return a placeholder image on error
            return self._create_placeholder_image(page_number)

    def generate_all_illustrations(self, story_data, art_style=None, progress_callback=None):
        """
        Generate illustrations for all pages in a story

        Args:
            story_data: Story dict from StoryGenerator with pages and character_descriptions
            art_style: Optional art style override
            progress_callback: Optional function to call with progress updates

        Returns:
            List of PIL Image objects, one per page
        """
        images = []
        pages = story_data.get('pages', [])
        character_descriptions = story_data.get('character_descriptions', {})

        for i, page in enumerate(pages):
            if progress_callback:
                progress_callback(i + 1, len(pages))

            scene_desc = page.get('scene_description', page.get('text', ''))
            page_num = page.get('page_number', i + 1)

            image = self.generate_page_illustration(
                scene_description=scene_desc,
                character_descriptions=character_descriptions,
                page_number=page_num,
                art_style=art_style
            )
            images.append(image)

        return images

    def _create_placeholder_image(self, page_number):
        """Create a placeholder image when generation fails"""
        from PIL import Image, ImageDraw, ImageFont

        img = Image.new('RGB', (1024, 1024), color='lightblue')
        draw = ImageDraw.Draw(img)

        # Draw some simple shapes
        draw.rectangle([50, 50, 974, 974], outline='darkblue', width=5)
        draw.text(
            (512, 512),
            f"Illustration\nPage {page_number}",
            fill='darkblue',
            anchor='mm'
        )

        return img

    def save_images(self, images, output_dir, prefix="page"):
        """
        Save images to directory

        Args:
            images: List of PIL Image objects
            output_dir: Directory to save images
            prefix: Filename prefix (default: "page")

        Returns:
            List of saved file paths
        """
        import os
        os.makedirs(output_dir, exist_ok=True)

        saved_paths = []
        for i, img in enumerate(images):
            filename = f"{prefix}_{i+1:02d}.png"
            filepath = os.path.join(output_dir, filename)
            img.save(filepath, 'PNG')
            saved_paths.append(filepath)

        return saved_paths

    def create_pdf_reader(self, story_data, images, output_path):
        """
        Create a PDF of the complete reader with text and illustrations

        Args:
            story_data: Story dict with title and pages
            images: List of PIL Images for each page
            output_path: Path to save the PDF

        Returns:
            Path to saved PDF
        """
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        from reportlab.lib.utils import ImageReader
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.lib.units import inch
        import textwrap

        # Create PDF
        c = canvas.Canvas(output_path, pagesize=letter)
        width, height = letter

        # Title page
        c.setFont("Helvetica-Bold", 36)
        title = story_data.get('title', 'Leveled Reader')
        c.drawCentredString(width / 2, height - 2 * inch, title)
        c.showPage()

        # Story pages
        pages = story_data.get('pages', [])
        for i, (page_data, image) in enumerate(zip(pages, images)):
            # Save image temporarily
            img_buffer = BytesIO()
            image.save(img_buffer, format='PNG')
            img_buffer.seek(0)
            img_reader = ImageReader(img_buffer)

            # Add image (top 2/3 of page)
            img_width = 6 * inch
            img_height = 6 * inch
            x = (width - img_width) / 2
            y = height - img_height - 1 * inch
            c.drawImage(img_reader, x, y, width=img_width, height=img_height)

            # Add text (bottom 1/3 of page)
            text = page_data.get('text', '')
            c.setFont("Helvetica", 14)

            # Wrap text
            wrapped_lines = textwrap.wrap(text, width=70)
            text_y = y - 0.5 * inch

            for line in wrapped_lines:
                c.drawCentredString(width / 2, text_y, line)
                text_y -= 0.3 * inch

            # Page number
            c.setFont("Helvetica", 10)
            c.drawCentredString(width / 2, 0.5 * inch, str(i + 1))

            c.showPage()

        c.save()
        return output_path
