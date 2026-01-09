# 📚 Custom Leveled Reader Creator

A powerful web application for creating custom educational readers tailored to specific reading levels, following established national standards and pedagogical best practices.

## 🌟 Features

- **Standards-Based Content**: Aligned with Guided Reading Levels (A-Z), Lexile Framework, and Common Core Standards
- **Flexible Input**: Creates engaging stories even with minimal information provided
- **Consistent AI Illustrations**: Maintains character consistency throughout the story
- **Multiple Reading Levels**: Supports Pre-K through 5th grade and beyond
- **Pedagogically Sound**: Stories designed following research-based best practices
- **Multiple Art Styles**: Choose from various illustration styles
- **Export Options**: Save as PDF or individual images

## 📋 Reading Levels Supported

| Level | Guided Reading | Grade | Lexile Range |
|-------|---------------|-------|--------------|
| Pre-K (Emergent Reader) | A-C | Pre-K to K | BR (Beginning Reader) |
| Kindergarten | D-E | K to 1st | BR to 200L |
| 1st Grade | F-I | 1st | 200L to 400L |
| 2nd Grade | J-M | 2nd | 400L to 600L |
| 3rd Grade | N-P | 3rd | 600L to 800L |
| 4th Grade | Q-S | 4th | 800L to 950L |
| 5th Grade and Above | T-Z | 5th+ | 950L to 1300L+ |

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- API keys for:
  - [Anthropic Claude](https://console.anthropic.com/) (for story generation)
  - [OpenAI](https://platform.openai.com/) (for image generation)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Reader
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API keys**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your API keys:
     ```
     ANTHROPIC_API_KEY=your_anthropic_api_key_here
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. **Run the application**:
   ```bash
   streamlit run app.py
   ```

6. **Open your browser** to `http://localhost:8501`

## 📖 How to Use

### Creating a Leveled Reader

1. **Select Reading Level**:
   - Choose the appropriate reading level from the sidebar
   - View detailed level specifications

2. **Add Characters**:
   - Enter character names and genders
   - Leave blank for auto-generated characters

3. **Story Direction** (Optional):
   - Answer guiding questions to shape your story:
     - Theme (e.g., friendship, adventure)
     - Setting (e.g., school, park, forest)
     - Problem/challenge
     - Lesson to teach
     - Special elements
     - Desired ending
   - **Note**: All fields are optional! The app will create a complete story even if nothing is filled in.

4. **Choose Illustration Style**:
   - Select from available art styles:
     - Default Children's Book
     - Watercolor
     - Cartoon
     - Realistic
     - Minimalist

5. **Generate**:
   - Click "Generate Leveled Reader"
   - Wait for story generation (30-60 seconds)
   - Wait for illustrations (2-3 minutes depending on page count)

6. **Review and Download**:
   - View your generated reader in the "Generated Reader" tab
   - Download as PDF or save individual images

## 🎓 Pedagogical Framework

### Reading Level Standards

Each reading level follows specific guidelines:

- **Vocabulary Complexity**: Age-appropriate word choices
- **Sentence Structure**: Complexity matched to reading level
- **Text Length**: Words per page appropriate for level
- **Concept Complexity**: Age-appropriate themes and ideas
- **Picture Support**: Varies by level (heavy support for early readers, minimal for advanced)

### Educational Features

- **Phonics Patterns**: Appropriate for the reading level
- **Sight Words**: Frequency matched to level expectations
- **Comprehension Skills**: Aligned with Common Core standards
- **Text Features**: Level-appropriate text structures

## 🏗️ Project Structure

```
Reader/
├── app.py                    # Main Streamlit application
├── story_generator.py        # AI story generation module
├── image_generator.py        # AI image generation module
├── reading_levels.py         # Reading level standards and pedagogy
├── requirements.txt          # Python dependencies
├── .env.example             # Example environment variables
├── .gitignore               # Git ignore rules
├── README.md                # This file
└── generated_readers/       # Output directory (created automatically)
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following:

```env
# Required API Keys
ANTHROPIC_API_KEY=your_anthropic_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

### API Key Setup

#### Anthropic Claude API

1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create a new API key
5. Copy the key to your `.env` file

#### OpenAI API

1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create a new API key
5. Copy the key to your `.env` file

**Note**: Both services require payment/credits. Check their pricing:
- [Anthropic Pricing](https://www.anthropic.com/api)
- [OpenAI Pricing](https://openai.com/pricing)

## 💡 Examples

### Minimal Input Example

- **Reading Level**: Kindergarten
- **Characters**: 1 character (name left blank)
- **Story Direction**: All fields blank

The app will generate a complete, age-appropriate story with consistent illustrations.

### Detailed Input Example

- **Reading Level**: 2nd Grade
- **Characters**:
  - Name: Emma, Gender: girl
  - Name: Max, Gender: boy
- **Story Direction**:
  - Theme: friendship
  - Setting: a magical library
  - Problem: The characters need to find a special book
  - Lesson: working together
  - Special Elements: talking animals
  - Ending: They succeed and become best friends

The app will generate a story incorporating all these elements.

## 🎨 Illustration Styles

Choose from several art styles:

- **Default (Children's Book)**: Classic children's book illustration style
- **Watercolor**: Soft, gentle watercolor effects
- **Cartoon**: Bold, playful cartoon style
- **Realistic**: More detailed and lifelike
- **Minimalist**: Simple shapes and limited colors

## ⚠️ Important Notes

### API Costs

- Story generation uses Claude API (typically $0.05-0.15 per story)
- Image generation uses DALL-E 3 (typically $0.04 per image)
- A complete 8-page reader costs approximately $0.40-0.50

### Generation Time

- Story generation: 30-60 seconds
- Image generation: 20-30 seconds per page
- Total time for 8-page reader: 3-5 minutes

### Character Consistency

The application provides detailed character descriptions to maintain visual consistency across illustrations. However, AI image generation may have slight variations.

### Content Safety

The application uses AI models with built-in content safety features. All generated content is designed to be age-appropriate for children.

## 🐛 Troubleshooting

### API Key Errors

**Error**: "ANTHROPIC_API_KEY must be set"
- **Solution**: Ensure `.env` file exists with valid API keys
- Restart the application after adding keys

### Image Generation Failures

**Error**: Individual images fail to generate
- **Solution**: The app will create placeholder images and continue
- Check OpenAI API credits and rate limits

### Module Import Errors

**Error**: "ModuleNotFoundError"
- **Solution**: Ensure all dependencies are installed:
  ```bash
  pip install -r requirements.txt
  ```

### Memory Issues

**Error**: Out of memory errors with multiple pages
- **Solution**: Generate readers with fewer pages or reduce image quality in code

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Additional reading level frameworks
- More illustration styles
- Multilingual support
- Additional export formats
- Character builder with visual customization
- Template story structures

## 📝 License

This project is provided as-is for educational purposes.

## 🙏 Acknowledgments

- **Reading Level Standards**: Based on Fountas & Pinnell, Lexile Framework, and Common Core State Standards
- **AI Models**: Powered by Anthropic Claude and OpenAI DALL-E
- **Framework**: Built with Streamlit

## 📞 Support

For issues, questions, or suggestions:
- Open an issue in the repository
- Check the troubleshooting section above
- Review API documentation for provider-specific issues

## 🔄 Updates and Roadmap

### Current Version: 1.0.0

### Planned Features:
- [ ] Save/load character presets
- [ ] Story templates by genre
- [ ] Batch generation
- [ ] Multilingual support
- [ ] Audio narration
- [ ] Interactive elements
- [ ] Teacher dashboard
- [ ] Student progress tracking

---

**Happy Reading! 📚✨**
