"""
Custom Leveled Reader Creator
A Streamlit application for creating custom leveled readers based on national standards
"""

import streamlit as st
import os
from datetime import datetime
from story_generator import StoryGenerator
from image_generator import ImageGenerator
from reading_levels import get_all_levels, get_level_info
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Custom Leveled Reader Creator",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
        height: 3em;
        border-radius: 10px;
        font-size: 1.2rem;
        font-weight: bold;
    }
    .character-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize session state variables"""
    if 'generated_story' not in st.session_state:
        st.session_state.generated_story = None
    if 'generated_images' not in st.session_state:
        st.session_state.generated_images = None
    if 'num_characters' not in st.session_state:
        st.session_state.num_characters = 2


def check_api_keys():
    """Check if required API keys are set"""
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")

    if not anthropic_key or not openai_key:
        st.error("⚠️ API Keys Not Found!")
        st.warning("""
        Please set up your API keys to use this application:

        1. Create a `.env` file in the application directory
        2. Add your API keys:
           ```
           ANTHROPIC_API_KEY=your_anthropic_key_here
           OPENAI_API_KEY=your_openai_key_here
           ```
        3. Restart the application

        You can get API keys from:
        - Anthropic Claude: https://console.anthropic.com/
        - OpenAI: https://platform.openai.com/
        """)
        return False
    return True


def main():
    """Main application"""
    initialize_session_state()

    # Header
    st.markdown('<h1 class="main-header">📚 Custom Leveled Reader Creator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Create custom educational readers based on national standards and best pedagogical practices</p>', unsafe_allow_html=True)

    # Check API keys
    if not check_api_keys():
        st.stop()

    # Sidebar - Reading Level Selection
    st.sidebar.header("📊 Reading Level")
    available_levels = get_all_levels()
    selected_level = st.sidebar.selectbox(
        "Select Target Reading Level",
        available_levels,
        help="Choose the appropriate reading level for your student(s)"
    )

    # Show level details
    level_info = get_level_info(selected_level)
    if level_info:
        with st.sidebar.expander("📖 Level Details", expanded=False):
            st.write(f"**Guided Reading:** {level_info['guided_reading']}")
            st.write(f"**Grade:** {level_info['grade_equivalent']}")
            st.write(f"**Lexile:** {level_info['lexile']}")
            st.write(f"**Words/Page:** {level_info['characteristics']['words_per_page']}")

    # Sidebar - Art Style
    st.sidebar.header("🎨 Illustration Style")
    art_style_options = {
        "Default (Children's Book)": None,
        "Watercolor": "watercolor children's book illustration, soft colors, gentle brush strokes",
        "Cartoon": "cartoon style children's book illustration, bold colors, playful characters",
        "Realistic": "realistic children's book illustration, detailed, lifelike",
        "Minimalist": "minimalist children's book illustration, simple shapes, limited color palette"
    }
    selected_art_style = st.sidebar.selectbox(
        "Choose Illustration Style",
        list(art_style_options.keys())
    )
    art_style = art_style_options[selected_art_style]

    # Main content area
    tab1, tab2, tab3 = st.tabs(["📝 Story Setup", "📚 Generated Reader", "ℹ️ About"])

    with tab1:
        st.header("Story Configuration")

        # Characters Section
        st.subheader("👥 Characters")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write("Add characters to your story. You can leave fields blank and the app will still create a story.")
        with col2:
            num_chars = st.number_input("Number of Characters", min_value=1, max_value=10, value=st.session_state.num_characters)
            st.session_state.num_characters = num_chars

        characters = []
        for i in range(num_chars):
            with st.container():
                st.markdown(f'<div class="character-box">', unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    char_name = st.text_input(
                        f"Character {i+1} Name",
                        key=f"char_name_{i}",
                        placeholder=f"Character {i+1} (optional)"
                    )
                with col2:
                    char_gender = st.selectbox(
                        f"Character {i+1} Gender",
                        ["boy", "girl", "non-binary", "unspecified"],
                        key=f"char_gender_{i}"
                    )
                st.markdown('</div>', unsafe_allow_html=True)

                # Use defaults if not provided
                if not char_name:
                    char_name = f"Character{i+1}"

                characters.append({"name": char_name, "gender": char_gender})

        st.divider()

        # Story Prompts Section
        st.subheader("📖 Story Direction (Optional)")
        st.write("Answer any questions you'd like. Blank answers are fine - the app will create a story regardless!")

        col1, col2 = st.columns(2)
        with col1:
            theme = st.text_input(
                "What theme should the story have?",
                placeholder="e.g., friendship, adventure, learning, family (optional)"
            )
            setting = st.text_input(
                "Where does the story take place?",
                placeholder="e.g., school, park, home, forest (optional)"
            )
            problem = st.text_area(
                "What challenge or problem do the characters face?",
                placeholder="Optional - leave blank for AI to decide"
            )

        with col2:
            lesson = st.text_input(
                "What lesson should the story teach?",
                placeholder="e.g., sharing, kindness, perseverance (optional)"
            )
            special_elements = st.text_input(
                "Any special elements to include?",
                placeholder="e.g., animals, magical items, vehicles (optional)"
            )
            ending = st.text_input(
                "How should the story end?",
                placeholder="Optional - leave blank for AI to decide"
            )

        story_prompts = {
            "theme": theme,
            "setting": setting,
            "problem": problem,
            "lesson": lesson,
            "special_elements": special_elements,
            "ending": ending
        }

        st.divider()

        # Generate Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("✨ Generate Leveled Reader"):
                with st.spinner("🎨 Creating your custom leveled reader..."):
                    try:
                        # Generate story
                        st.info("📝 Generating story content...")
                        story_gen = StoryGenerator()
                        story_data = story_gen.generate_story(
                            reading_level=selected_level,
                            characters=characters,
                            story_prompts=story_prompts,
                            theme=theme if theme else None
                        )
                        st.session_state.generated_story = story_data

                        # Generate images
                        st.info("🎨 Creating illustrations...")
                        image_gen = ImageGenerator()

                        progress_bar = st.progress(0)
                        progress_text = st.empty()

                        def progress_callback(current, total):
                            progress = current / total
                            progress_bar.progress(progress)
                            progress_text.text(f"Generating illustration {current} of {total}...")

                        images = image_gen.generate_all_illustrations(
                            story_data,
                            art_style=art_style,
                            progress_callback=progress_callback
                        )
                        st.session_state.generated_images = images

                        progress_bar.empty()
                        progress_text.empty()

                        st.success("✅ Your leveled reader is ready! Check the 'Generated Reader' tab.")
                        st.balloons()

                    except Exception as e:
                        st.error(f"❌ Error generating reader: {str(e)}")
                        st.exception(e)

    with tab2:
        st.header("Your Generated Reader")

        if st.session_state.generated_story and st.session_state.generated_images:
            story = st.session_state.generated_story
            images = st.session_state.generated_images

            # Display title
            st.markdown(f"## {story.get('title', 'Untitled')}")
            st.markdown(f"*{selected_level} Level Reader*")
            st.divider()

            # Display pages
            pages = story.get('pages', [])
            for i, (page_data, image) in enumerate(zip(pages, images)):
                col1, col2 = st.columns([1, 1])

                with col1:
                    st.image(image, use_container_width=True)

                with col2:
                    st.markdown(f"### Page {page_data.get('page_number', i+1)}")
                    st.markdown(f"*{page_data.get('text', '')}*")

                st.divider()

            # Download options
            st.subheader("📥 Download Options")
            col1, col2 = st.columns(2)

            with col1:
                if st.button("💾 Save as PDF"):
                    with st.spinner("Creating PDF..."):
                        try:
                            output_dir = "generated_readers"
                            os.makedirs(output_dir, exist_ok=True)
                            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                            pdf_path = os.path.join(output_dir, f"reader_{timestamp}.pdf")

                            image_gen = ImageGenerator()
                            image_gen.create_pdf_reader(story, images, pdf_path)

                            with open(pdf_path, "rb") as f:
                                st.download_button(
                                    label="📄 Download PDF",
                                    data=f,
                                    file_name=f"leveled_reader_{timestamp}.pdf",
                                    mime="application/pdf"
                                )
                            st.success(f"✅ PDF created: {pdf_path}")
                        except Exception as e:
                            st.error(f"Error creating PDF: {str(e)}")

            with col2:
                if st.button("🖼️ Save Individual Images"):
                    with st.spinner("Saving images..."):
                        try:
                            output_dir = "generated_readers"
                            os.makedirs(output_dir, exist_ok=True)
                            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                            img_dir = os.path.join(output_dir, f"images_{timestamp}")

                            image_gen = ImageGenerator()
                            saved_paths = image_gen.save_images(images, img_dir)

                            st.success(f"✅ {len(saved_paths)} images saved to: {img_dir}")
                        except Exception as e:
                            st.error(f"Error saving images: {str(e)}")

        else:
            st.info("👈 Create a reader in the 'Story Setup' tab to see it here!")

    with tab3:
        st.header("About This Application")

        st.markdown("""
        ### 📚 Custom Leveled Reader Creator

        This application creates custom educational readers tailored to specific reading levels,
        following established national standards and pedagogical best practices.

        #### Features:
        - **Standards-Based**: Aligned with Guided Reading Levels, Lexile Framework, and Common Core Standards
        - **Flexible Input**: Works even with minimal information provided
        - **Consistent Illustrations**: AI-generated images maintain character consistency
        - **Multiple Reading Levels**: From Pre-K through 5th grade and beyond
        - **Pedagogically Sound**: Stories designed with educational best practices

        #### How It Works:
        1. **Select Reading Level**: Choose the appropriate level for your student(s)
        2. **Add Characters**: Provide character names and genders (optional)
        3. **Story Direction**: Answer guiding questions to shape the story (optional)
        4. **Generate**: Click the generate button and wait for AI to create your reader
        5. **Download**: Save as PDF or individual images

        #### Reading Level Standards:
        The application uses comprehensive reading level frameworks including:
        - **Guided Reading Levels (A-Z)**: Fountas & Pinnell framework
        - **Lexile Measures**: MetaMetrics Framework
        - **Grade Level Equivalents**: K-5+
        - **Common Core Alignment**: Age-appropriate skills and concepts

        #### Technology:
        - **AI Story Generation**: Claude by Anthropic
        - **AI Illustration**: DALL-E by OpenAI
        - **Interface**: Streamlit
        - **Standards**: Research-based reading pedagogy

        #### Privacy & Data:
        - Stories are generated fresh each time
        - No user data is stored
        - API calls are made securely

        ---

        **Note**: This application requires API keys for Anthropic Claude and OpenAI.
        See the setup instructions in the README for configuration details.
        """)


if __name__ == "__main__":
    main()
