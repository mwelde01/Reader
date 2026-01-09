# 🧪 Step-by-Step Testing Guide

Complete guide to test the Custom Leveled Reader Creator application.

## Prerequisites Checklist

Before you begin, ensure you have:
- [ ] Computer with internet connection
- [ ] Python 3.8 or higher installed
- [ ] Credit card for API services (or free trial credits)
- [ ] Text editor (VS Code, Sublime, Notepad++, etc.)
- [ ] Terminal/Command Prompt access

---

## Phase 1: Environment Setup (15 minutes)

### Step 1: Verify Python Installation

Open your terminal/command prompt and run:

```bash
python --version
```

**Expected output**: `Python 3.8.x` or higher

**If Python is not installed**:
- Download from [python.org](https://www.python.org/downloads/)
- Install with "Add to PATH" option checked
- Restart terminal and verify again

### Step 2: Navigate to Project Directory

```bash
cd /home/user/Reader
```

**Or on your local machine**:
```bash
cd path/to/Reader
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

**Expected output**: A new `venv` folder is created

**Wait**: 30-60 seconds for creation

### Step 4: Activate Virtual Environment

**On Mac/Linux**:
```bash
source venv/bin/activate
```

**On Windows**:
```bash
venv\Scripts\activate
```

**Expected output**: Your prompt should now show `(venv)` at the beginning

**If activation fails on Windows**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating again.

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

**Expected output**:
- Multiple "Successfully installed..." messages
- Should take 1-2 minutes

**Verify installation**:
```bash
pip list
```

**You should see**:
- streamlit
- anthropic
- openai
- pillow
- requests
- python-dotenv

---

## Phase 2: API Key Setup (10 minutes)

### Step 6: Get Anthropic Claude API Key

1. **Go to**: https://console.anthropic.com/
2. **Sign up** or log in
3. **Click**: "API Keys" in the left sidebar
4. **Click**: "Create Key" button
5. **Name it**: "Reader App Test"
6. **Copy**: The entire key (starts with `sk-ant-api03-`)
7. **Save**: Paste it temporarily in a text file

**Important**: This key will only be shown once!

**Cost**: Anthropic offers $5 in free credits for new users

### Step 7: Get OpenAI API Key

1. **Go to**: https://platform.openai.com/
2. **Sign up** or log in
3. **Click**: Your profile icon → "View API keys"
4. **Click**: "Create new secret key"
5. **Name it**: "Reader App Test"
6. **Copy**: The entire key (starts with `sk-`)
7. **Save**: Paste it in your text file

**Important**: This key will only be shown once!

**Cost**: OpenAI offers $5 in free credits for new users (expires after 3 months)

### Step 8: Create Environment File

In the Reader directory, copy the example file:

```bash
cp .env.example .env
```

**Or manually create** a new file named `.env`

### Step 9: Add API Keys to .env File

Open `.env` in your text editor and add your keys:

```env
ANTHROPIC_API_KEY=sk-ant-api03-YOUR-ACTUAL-KEY-HERE
OPENAI_API_KEY=sk-YOUR-ACTUAL-KEY-HERE
```

**Important**:
- Replace the placeholder text with your actual keys
- No spaces around the `=` sign
- No quotes around the keys
- Save the file

**Verify the file**:
```bash
cat .env
```

**You should see** your two API keys displayed.

---

## Phase 3: Launch the Application (2 minutes)

### Step 10: Start Streamlit

```bash
streamlit run app.py
```

**Expected output**:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

**What happens**:
- Your default browser should open automatically
- You'll see the "Custom Leveled Reader Creator" interface
- The app should load without errors

**If the browser doesn't open automatically**:
- Manually go to: http://localhost:8501

**If you see an error about API keys**:
- Stop the app (Ctrl+C in terminal)
- Double-check your `.env` file
- Make sure there are no extra spaces or quotes
- Restart: `streamlit run app.py`

---

## Phase 4: Test Case 1 - Minimal Input (5 minutes)

**Goal**: Verify the app works with almost no input

### Step 11: Configure Minimal Settings

1. **Sidebar - Reading Level**: Select "Kindergarten"
2. **Sidebar - Illustration Style**: Leave as "Default (Children's Book)"
3. **Story Setup Tab**:
   - Leave "Character 1 Name" blank
   - Leave "Character 1 Gender" as default (boy)
   - Leave all story direction questions blank

### Step 12: Generate First Reader

1. **Click**: "✨ Generate Leveled Reader" button
2. **Watch**: Progress messages appear
   - "📝 Generating story content..."
   - "🎨 Creating illustrations..."
   - Progress bar shows image generation

**Expected time**: 3-5 minutes total
- Story generation: 30-60 seconds
- Image generation: 2-4 minutes

**What to watch for**:
- No error messages appear
- Progress bar moves smoothly
- Eventually see "✅ Your leveled reader is ready!"
- Balloons animation plays

### Step 13: Review Generated Reader

1. **Click**: "📚 Generated Reader" tab
2. **Verify**:
   - [ ] Story has a title
   - [ ] Multiple pages are displayed (typically 6-10)
   - [ ] Each page has an illustration
   - [ ] Each page has text below the image
   - [ ] Text is appropriate for kindergarten level
   - [ ] Images are colorful and child-appropriate

**Check story quality**:
- [ ] Story has a clear beginning, middle, and end
- [ ] Sentences are short and simple
- [ ] Vocabulary is age-appropriate
- [ ] Story makes sense even without character input

**Check image quality**:
- [ ] Images are clear and colorful
- [ ] Images match the text content
- [ ] Character appearance is reasonably consistent

### Step 14: Test PDF Export

1. **Scroll down** to "📥 Download Options"
2. **Click**: "💾 Save as PDF"
3. **Wait**: 5-10 seconds for PDF creation
4. **Click**: "📄 Download PDF" button
5. **Verify**:
   - [ ] PDF downloads successfully
   - [ ] Can open the PDF
   - [ ] PDF contains all pages
   - [ ] Images and text are visible

**Expected file size**: 5-15 MB

### Step 15: Test Image Export

1. **Click**: "🖼️ Save Individual Images"
2. **Wait**: 2-3 seconds
3. **Verify**: Success message shows directory path
4. **Check in terminal**: Look for the saved file location
5. **Navigate to**: `generated_readers/images_[timestamp]/`
6. **Verify**:
   - [ ] Folder exists
   - [ ] Contains multiple PNG files (one per page)
   - [ ] Images open correctly

---

## Phase 5: Test Case 2 - Full Custom Input (5 minutes)

**Goal**: Test with complete character and story customization

### Step 16: Configure Custom Settings

1. **Sidebar - Reading Level**: Select "2nd Grade"
2. **Sidebar - Illustration Style**: Select "Cartoon"
3. **Story Setup Tab**:
   - **Number of Characters**: Change to 2
   - **Character 1 Name**: "Emma"
   - **Character 1 Gender**: "girl"
   - **Character 2 Name**: "Max"
   - **Character 2 Gender**: "boy"
4. **Story Direction**:
   - **Theme**: "friendship and teamwork"
   - **Setting**: "a magical library"
   - **Problem**: "They need to find a special book to help their teacher"
   - **Lesson**: "working together makes hard tasks easier"
   - **Special elements**: "talking owl, floating books"
   - **Ending**: "They find the book and become best friends"

### Step 17: Generate Custom Reader

1. **Click**: "✨ Generate Leveled Reader"
2. **Wait**: 4-6 minutes
3. **Watch for**: Same progress indicators as before

**Expected differences**:
- More pages (8-12 for 2nd grade)
- More complex sentences
- Longer text per page
- Cartoon-style illustrations

### Step 18: Verify Customization

1. **Check title**: Should reference the theme
2. **Check characters**: Both Emma and Max should appear
3. **Check setting**: Story should take place in a library
4. **Check elements**:
   - [ ] Owl character appears
   - [ ] Library setting is visible
   - [ ] Book-finding plot is present
   - [ ] Teamwork theme is evident
   - [ ] Positive ending is shown
5. **Check reading level**:
   - [ ] Longer sentences than kindergarten version
   - [ ] More complex vocabulary
   - [ ] More detailed story

---

## Phase 6: Test Case 3 - Different Reading Levels (10 minutes)

**Goal**: Verify reading level standards are followed

### Step 19: Test Pre-K Level

1. **Sidebar - Reading Level**: "Pre-K (Emergent Reader)"
2. **Configure**:
   - 1 character (any name)
   - Theme: "animals"
   - All other fields blank
3. **Generate** and verify:
   - [ ] Very few words per page (1-3)
   - [ ] Very simple sentences
   - [ ] High picture support
   - [ ] Repetitive text patterns

### Step 20: Test 4th Grade Level

1. **Sidebar - Reading Level**: "4th Grade"
2. **Configure**:
   - 2-3 characters
   - Theme: "mystery adventure"
   - Setting: "ancient ruins"
3. **Generate** and verify:
   - [ ] Much longer text per page
   - [ ] Complex sentences
   - [ ] Advanced vocabulary
   - [ ] Detailed plot

### Step 21: Compare Levels Side by Side

**Open multiple readers** (if you saved PDFs) and compare:

| Feature | Pre-K | 2nd Grade | 4th Grade |
|---------|-------|-----------|-----------|
| Words/page | 1-3 | 15-30 | 50-100 |
| Sentence complexity | Very simple | Moderate | Complex |
| Vocabulary | Basic | Growing | Advanced |
| Story length | 6-8 pages | 8-10 pages | 10-15 pages |

---

## Phase 7: Edge Cases and Error Testing (10 minutes)

### Step 22: Test with Maximum Characters

1. **Number of Characters**: Set to 10
2. **Name all characters**: Character1, Character2, etc.
3. **Generate**
4. **Verify**:
   - [ ] Story includes multiple characters
   - [ ] No errors occur
   - [ ] May take longer to generate

### Step 23: Test Special Characters in Names

1. **Character names**: Try "José", "María", "François"
2. **Generate**
3. **Verify**:
   - [ ] Special characters display correctly
   - [ ] No encoding errors

### Step 24: Test Very Long Input

1. **Problem field**: Write a paragraph (200+ words)
2. **Generate**
3. **Verify**:
   - [ ] App doesn't crash
   - [ ] Story incorporates key elements
   - [ ] No truncation errors

### Step 25: Test Rapid Regeneration

1. **Generate a story**
2. **Immediately click** "Generate Leveled Reader" again
3. **Verify**:
   - [ ] New story generates successfully
   - [ ] Old story is replaced
   - [ ] No conflicts or caching issues

---

## Phase 8: Performance and Cost Testing (5 minutes)

### Step 26: Monitor Generation Time

For each reading level, record:

| Level | Story Time | Image Time | Total Time |
|-------|-----------|------------|------------|
| Pre-K | ___ sec | ___ sec | ___ min |
| Kindergarten | ___ sec | ___ sec | ___ min |
| 1st Grade | ___ sec | ___ sec | ___ min |
| 2nd Grade | ___ sec | ___ sec | ___ min |

**Expected ranges**:
- Story: 30-90 seconds
- Images: 2-4 minutes (for 6-10 pages)
- Total: 3-6 minutes

### Step 27: Check API Usage

**Anthropic Console**:
1. Go to https://console.anthropic.com/
2. Click "Usage"
3. **Record**: How much credit was used
4. **Expected**: $0.05-0.15 per story

**OpenAI Console**:
1. Go to https://platform.openai.com/usage
2. View usage dashboard
3. **Record**: How much credit was used
4. **Expected**: $0.32-0.48 per story (8 images × $0.04)

**Total cost per reader**: ~$0.40-0.65

---

## Phase 9: Illustration Consistency Testing (5 minutes)

### Step 28: Test Character Consistency

1. **Generate a story** with 1-2 named characters
2. **Review all images** carefully
3. **Check**:
   - [ ] Character has consistent hair color
   - [ ] Character has consistent clothing style
   - [ ] Character has consistent appearance
   - [ ] Character's age looks consistent

**Note**: Some variation is expected with current AI technology, but major features should stay consistent.

### Step 29: Test Different Art Styles

Generate the same story setup with different styles:

1. **Default**: Note the illustration style
2. **Watercolor**: Verify softer, painted appearance
3. **Cartoon**: Verify bold, playful style
4. **Realistic**: Verify more detailed, lifelike style
5. **Minimalist**: Verify simpler, cleaner style

---

## Phase 10: Error Handling (5 minutes)

### Step 30: Test Without API Keys

1. **Stop the app** (Ctrl+C)
2. **Rename** `.env` to `.env.backup`
3. **Restart**: `streamlit run app.py`
4. **Verify**:
   - [ ] Clear error message appears
   - [ ] Instructions for fixing are shown
   - [ ] App doesn't crash

5. **Fix**: Rename `.env.backup` back to `.env`
6. **Restart** the app

### Step 31: Test with Invalid API Key

1. **Stop the app**
2. **Edit** `.env` and change one character in a key
3. **Restart** the app
4. **Try to generate** a reader
5. **Verify**:
   - [ ] Error message appears
   - [ ] Error mentions authentication/API key
   - [ ] App doesn't crash completely

6. **Fix**: Restore correct API key
7. **Restart** the app

### Step 32: Test Network Issues

**This test is optional** - only if you can safely disconnect:

1. **Start generating** a reader
2. **Disconnect internet** mid-generation
3. **Verify**:
   - [ ] Error message appears
   - [ ] App remains responsive
   - [ ] Can retry after reconnecting

---

## Phase 11: UI/UX Testing (5 minutes)

### Step 33: Test Responsive Design

1. **Resize browser window** to different widths
2. **Verify**:
   - [ ] Layout adjusts appropriately
   - [ ] No overlapping text
   - [ ] Buttons remain clickable
   - [ ] Images scale properly

### Step 34: Test Tab Navigation

1. **Click through all tabs**: Story Setup → Generated Reader → About
2. **Verify**:
   - [ ] All tabs load without errors
   - [ ] Content displays correctly
   - [ ] Navigation is smooth

### Step 35: Test Sidebar Functionality

1. **Expand/collapse** "Level Details"
2. **Change settings** and verify they're applied
3. **Verify**:
   - [ ] Sidebar stays visible
   - [ ] Settings persist during generation
   - [ ] No visual glitches

---

## Phase 12: Final Validation (5 minutes)

### Step 36: Educational Content Review

**Generate one final reader** and evaluate:

**Pedagogical Quality**:
- [ ] Content is age-appropriate
- [ ] Vocabulary matches reading level
- [ ] Sentence structure is appropriate
- [ ] Story has educational value
- [ ] Theme is positive and constructive

**Illustration Quality**:
- [ ] Images are child-appropriate
- [ ] No inappropriate content
- [ ] Clear and easy to understand
- [ ] Support the text content

### Step 37: Complete Test Report

**Fill out this checklist**:

#### Functionality
- [ ] App launches without errors
- [ ] Story generation works
- [ ] Image generation works
- [ ] PDF export works
- [ ] Image export works
- [ ] All reading levels work
- [ ] All art styles work

#### Quality
- [ ] Stories are coherent and engaging
- [ ] Reading levels are accurate
- [ ] Images are appropriate and consistent
- [ ] Text matches illustrations

#### Performance
- [ ] Generation completes in expected time
- [ ] No crashes or freezes
- [ ] Memory usage is reasonable
- [ ] API costs are within expected range

#### User Experience
- [ ] UI is intuitive and clear
- [ ] Error messages are helpful
- [ ] Documentation is accurate
- [ ] Instructions are easy to follow

---

## Troubleshooting During Testing

If you encounter issues, check:

1. **TROUBLESHOOTING.md** in the project directory
2. **Terminal output** for specific error messages
3. **API key validity** in provider dashboards
4. **Internet connection** stability
5. **Python version** compatibility

Common issues:
- **"Module not found"**: Run `pip install -r requirements.txt`
- **"API key error"**: Check `.env` file format
- **"Generation takes too long"**: This is normal for first generation
- **"Images inconsistent"**: This is a limitation of current AI technology

---

## Test Completion

### You've successfully completed testing if:

✅ Generated at least 3 different readers
✅ Tested multiple reading levels
✅ Exported PDF and images successfully
✅ Verified content quality
✅ Confirmed API costs are reasonable
✅ Documented any issues found

### Next Steps:

1. **Review** any issues found
2. **Document** unexpected behavior
3. **Share** feedback or bug reports
4. **Start using** the app for real educational content!

---

## Expected Test Duration

| Phase | Time | Cumulative |
|-------|------|------------|
| Environment Setup | 15 min | 15 min |
| API Key Setup | 10 min | 25 min |
| Launch Application | 2 min | 27 min |
| Test Case 1 (Minimal) | 5 min | 32 min |
| Test Case 2 (Custom) | 5 min | 37 min |
| Test Case 3 (Levels) | 10 min | 47 min |
| Edge Cases | 10 min | 57 min |
| Performance Testing | 5 min | 62 min |
| Illustration Testing | 5 min | 67 min |
| Error Handling | 5 min | 72 min |
| UI/UX Testing | 5 min | 77 min |
| Final Validation | 5 min | 82 min |

**Total estimated time**: 80-90 minutes (including generation wait times)

---

## Cost Estimate for Full Testing

Assuming you generate 5-6 complete readers during testing:

- **Anthropic Claude**: $0.30-0.90 (story generation)
- **OpenAI DALL-E**: $1.60-2.40 (image generation)
- **Total**: $2.00-3.30

Both services offer $5 in free credits for new users, which is sufficient for complete testing.

---

**Good luck with your testing! 🧪📚**
