# ⚡ Quick Test Checklist

Fast reference for testing the Custom Leveled Reader Creator.

## 🚀 Quick Start Test (10 minutes)

### 1. Setup (2 min)
```bash
cd Reader
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure API Keys (2 min)
```bash
cp .env.example .env
# Edit .env and add your API keys
```

### 3. Launch (1 min)
```bash
streamlit run app.py
# Opens at http://localhost:8501
```

### 4. Generate Test Reader (5 min)
- Reading Level: "Kindergarten"
- Leave all fields default/blank
- Click "Generate Leveled Reader"
- Wait 3-5 minutes
- Check "Generated Reader" tab

### ✅ Success Criteria
- [ ] App launches without errors
- [ ] Story generates successfully
- [ ] Images appear on all pages
- [ ] Can download PDF

---

## 📋 Full Test Checklist

### Environment
- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] All dependencies installed
- [ ] `.env` file created with API keys

### API Configuration
- [ ] Anthropic API key obtained
- [ ] OpenAI API key obtained
- [ ] Keys added to `.env` correctly
- [ ] App recognizes keys (no errors on startup)

### Basic Functionality
- [ ] App launches successfully
- [ ] UI loads without errors
- [ ] Sidebar controls work
- [ ] All tabs accessible

### Story Generation
- [ ] Pre-K level works
- [ ] Kindergarten level works
- [ ] 1st Grade level works
- [ ] 2nd Grade level works
- [ ] 3rd Grade level works
- [ ] 4th Grade level works
- [ ] 5th Grade+ level works

### Character Input
- [ ] Single character works
- [ ] Multiple characters work
- [ ] Blank character names work
- [ ] Different genders work
- [ ] Special characters in names work

### Story Customization
- [ ] Theme field affects story
- [ ] Setting field affects story
- [ ] Problem field affects story
- [ ] Lesson field affects story
- [ ] Special elements field affects story
- [ ] Ending field affects story
- [ ] All blank fields work (minimal input)

### Illustration Styles
- [ ] Default style works
- [ ] Watercolor style works
- [ ] Cartoon style works
- [ ] Realistic style works
- [ ] Minimalist style works

### Image Generation
- [ ] Images generate for all pages
- [ ] Characters appear consistently
- [ ] Images match text content
- [ ] Images are child-appropriate
- [ ] Images are clear and visible

### Export Functions
- [ ] PDF export works
- [ ] PDF contains all pages
- [ ] PDF is readable
- [ ] Individual image export works
- [ ] All images save correctly

### Reading Level Accuracy
- [ ] Pre-K: 1-3 words/page, very simple
- [ ] Kindergarten: 4-6 words/page, simple sentences
- [ ] 1st Grade: 7-15 words/page, longer sentences
- [ ] 2nd Grade: 15-30 words/page, complex structures
- [ ] 3rd Grade: 30-50 words/page, varied structures
- [ ] 4th Grade: 50-100 words/page, sophisticated
- [ ] 5th Grade+: 100+ words/page, mature writing

### Content Quality
- [ ] Stories are coherent
- [ ] Stories have beginning/middle/end
- [ ] Vocabulary is age-appropriate
- [ ] Sentences match reading level
- [ ] Themes are positive
- [ ] Content is educational
- [ ] No inappropriate content

### Error Handling
- [ ] Missing API keys show clear error
- [ ] Invalid API keys show clear error
- [ ] Network issues handled gracefully
- [ ] Generation errors don't crash app

### Performance
- [ ] Story generates in 30-90 seconds
- [ ] Images generate in 2-5 minutes
- [ ] Total time under 6 minutes
- [ ] App remains responsive during generation
- [ ] Memory usage is reasonable

### UI/UX
- [ ] Interface is intuitive
- [ ] Buttons are clearly labeled
- [ ] Progress indicators work
- [ ] Error messages are helpful
- [ ] Layout is clean and organized
- [ ] Responsive design works

---

## 🎯 Essential Tests (Minimum)

If time is limited, test these 3 scenarios:

### Test 1: Minimal Input
- **Level**: Kindergarten
- **Characters**: 1 (blank name)
- **Fields**: All blank
- **Expected**: Complete story with 6-8 pages

### Test 2: Full Custom
- **Level**: 2nd Grade
- **Characters**: Emma (girl), Max (boy)
- **Theme**: friendship
- **Setting**: magical library
- **Expected**: Story incorporating all elements

### Test 3: Advanced Level
- **Level**: 4th Grade
- **Characters**: 2-3 characters with names
- **Fields**: Fill in 2-3 fields
- **Expected**: Longer, more complex story

---

## 💰 Cost Tracking

Track your testing costs:

| Test # | Level | Pages | Story Cost | Image Cost | Total |
|--------|-------|-------|------------|------------|-------|
| 1 | | | $ | $ | $ |
| 2 | | | $ | $ | $ |
| 3 | | | $ | $ | $ |
| 4 | | | $ | $ | $ |
| 5 | | | $ | $ | $ |

**Expected per reader**: ~$0.40-0.65
**Total for 5 tests**: ~$2.00-3.25

---

## ⏱️ Time Estimates

| Task | Time |
|------|------|
| Environment setup | 5-15 min |
| API key setup | 5-10 min |
| First generation | 5 min |
| Each additional test | 4-6 min |
| Full test suite | 80-90 min |

---

## 🐛 Common Issues

| Issue | Quick Fix |
|-------|-----------|
| "Module not found" | `pip install -r requirements.txt` |
| "API key error" | Check `.env` format, no spaces/quotes |
| "Port already in use" | `streamlit run app.py --server.port 8502` |
| Generation hangs | Check internet, wait 5 min max |
| Images inconsistent | Expected behavior, regenerate if needed |

---

## ✅ Test Complete When:

- [ ] 3+ successful generations
- [ ] Multiple reading levels tested
- [ ] PDF export works
- [ ] No critical errors found
- [ ] Content quality verified
- [ ] API costs documented

---

## 📊 Test Report Template

```
TESTING SUMMARY
Date: ___________
Tester: ___________

RESULTS:
✅ Passed: ___ tests
⚠️  Warnings: ___ issues
❌ Failed: ___ tests

TOTAL COST: $_____
TOTAL TIME: ___ minutes

NOTES:
_________________________________
_________________________________
_________________________________

RECOMMENDATION:
[ ] Ready for use
[ ] Needs fixes
[ ] Requires more testing
```

---

For detailed testing procedures, see **TESTING_GUIDE.md**
