# 🚀 Quick Start Guide

Get your Custom Leveled Reader Creator up and running in 5 minutes!

## Step 1: Install Python

Make sure you have Python 3.8+ installed:
```bash
python --version
```

If not installed, download from [python.org](https://www.python.org/downloads/)

## Step 2: Set Up the Project

```bash
# Navigate to the project directory
cd Reader

# Create a virtual environment (recommended)
python -m venv venv

# Activate the virtual environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Step 3: Get API Keys

### Anthropic Claude API Key
1. Go to https://console.anthropic.com/
2. Sign up or log in
3. Click "API Keys" in the left sidebar
4. Click "Create Key"
5. Copy your API key

### OpenAI API Key
1. Go to https://platform.openai.com/
2. Sign up or log in
3. Click your profile icon → "View API keys"
4. Click "Create new secret key"
5. Copy your API key

## Step 4: Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your favorite text editor
# Add your API keys:
```

Edit `.env`:
```
ANTHROPIC_API_KEY=sk-ant-api03-xxxxx
OPENAI_API_KEY=sk-xxxxx
```

## Step 5: Run the App

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

## Step 6: Create Your First Reader

1. **Select Reading Level**: Choose "Kindergarten" from the sidebar
2. **Add a Character**:
   - Name: Sam
   - Gender: boy
3. **Story Direction** (optional):
   - Theme: friendship
   - Setting: playground
4. **Click**: "Generate Leveled Reader"
5. **Wait**: 3-5 minutes for generation
6. **View**: Check the "Generated Reader" tab
7. **Download**: Save as PDF

## 🎉 That's It!

You've created your first custom leveled reader!

## Next Steps

- Try different reading levels
- Experiment with multiple characters
- Leave fields blank to see what the AI creates
- Try different illustration styles
- Generate readers for different learning objectives

## Need Help?

- Check the full [README.md](README.md) for detailed documentation
- See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common issues
- Review example outputs in the `examples/` folder (if available)

## Estimated Costs

- One 8-page reader ≈ $0.40-0.50
- Story generation ≈ $0.05-0.15
- Images (8 pages) ≈ $0.32

Both Anthropic and OpenAI offer free trial credits for new users!
