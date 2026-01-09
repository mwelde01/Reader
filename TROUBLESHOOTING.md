# 🔧 Troubleshooting Guide

Common issues and their solutions.

## Installation Issues

### Issue: `pip install` fails

**Error**: `ERROR: Could not find a version that satisfies the requirement...`

**Solutions**:
1. Upgrade pip:
   ```bash
   pip install --upgrade pip
   ```

2. Check Python version:
   ```bash
   python --version  # Should be 3.8 or higher
   ```

3. Try installing packages individually:
   ```bash
   pip install streamlit
   pip install anthropic
   pip install openai
   ```

### Issue: Virtual environment not activating

**On Windows**:
If you get an execution policy error:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**On Mac/Linux**:
Make sure you're using the correct command:
```bash
source venv/bin/activate
```

## API Key Issues

### Issue: "ANTHROPIC_API_KEY must be set"

**Checklist**:
1. ✅ `.env` file exists in the project root
2. ✅ `.env` file contains `ANTHROPIC_API_KEY=your_key_here`
3. ✅ No spaces around the `=` sign
4. ✅ No quotes around the API key
5. ✅ Application restarted after adding keys

**Correct format**:
```
ANTHROPIC_API_KEY=sk-ant-api03-xxxxx
OPENAI_API_KEY=sk-xxxxx
```

**Incorrect formats**:
```
ANTHROPIC_API_KEY = sk-ant-api03-xxxxx  # ❌ spaces
ANTHROPIC_API_KEY="sk-ant-api03-xxxxx"  # ❌ quotes
```

### Issue: "Invalid API key"

**Solutions**:
1. Verify your API key in the provider's dashboard
2. Check for accidental spaces or newlines in `.env`
3. Make sure the key hasn't been revoked
4. Generate a new API key if needed

### Issue: "Rate limit exceeded"

**Solutions**:
1. Wait a few minutes before retrying
2. Check your API usage dashboard
3. Upgrade your API plan if needed
4. Reduce the number of pages generated

## Generation Issues

### Issue: Story generation takes too long

**Expected time**: 30-60 seconds

**If longer**:
1. Check your internet connection
2. Verify Anthropic API status: https://status.anthropic.com/
3. Try a different reading level (shorter stories generate faster)

### Issue: Image generation fails

**Symptoms**: Placeholder images appear instead of illustrations

**Solutions**:
1. Check OpenAI API credits: https://platform.openai.com/usage
2. Verify DALL-E 3 is available in your region
3. Check OpenAI status: https://status.openai.com/
4. Reduce the number of characters (complex prompts may fail)

### Issue: Images are inconsistent

**This is partially expected** with current AI image generation technology.

**To improve consistency**:
1. Use simpler character descriptions
2. Choose "Default" or "Cartoon" art styles
3. Use fewer characters (1-3 works best)
4. Keep character names distinct

### Issue: Story doesn't match reading level

**Solutions**:
1. Verify the correct reading level is selected
2. Try generating again (AI output varies)
3. Check if custom prompts are too complex for the level
4. Report consistent issues for investigation

## Application Issues

### Issue: Streamlit won't start

**Error**: `streamlit: command not found`

**Solution**:
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Reinstall streamlit
pip install streamlit
```

### Issue: Page won't load

**Solutions**:
1. Check if port 8501 is already in use:
   ```bash
   # Use a different port
   streamlit run app.py --server.port 8502
   ```

2. Clear browser cache

3. Try a different browser

### Issue: "Module not found" error

**Solution**:
```bash
# Reinstall all dependencies
pip install -r requirements.txt

# Or install the specific missing module
pip install <module-name>
```

## PDF Generation Issues

### Issue: PDF creation fails

**Error**: `No module named 'reportlab'`

**Solution**:
```bash
pip install reportlab
```

### Issue: PDF text is cut off

**This is a known limitation** with long text passages.

**Solutions**:
1. Generate a shorter story (lower reading level)
2. Manually adjust text in a PDF editor after generation
3. Use individual images instead and create PDF manually

## Performance Issues

### Issue: Application is slow

**Solutions**:
1. Close other applications
2. Reduce image quality (edit `image_generator.py`):
   ```python
   size="1024x1024"  # Change to "512x512"
   ```
3. Generate fewer pages
4. Upgrade your hardware (RAM and internet speed matter most)

### Issue: Out of memory

**Solutions**:
1. Restart the application
2. Generate shorter stories
3. Save and clear after each generation
4. Increase system memory/swap

## Content Issues

### Issue: Generated story is inappropriate

**This should be rare** due to built-in AI safety features.

**Solutions**:
1. Regenerate the story
2. Adjust prompts to be more specific
3. Review and manually edit before showing to children
4. Report consistent issues

### Issue: Story ignores my prompts

**Remember**: Prompts are guidelines, not strict rules.

**Solutions**:
1. Make prompts more specific
2. Use simpler language in prompts
3. Ensure prompts match the reading level
4. Try multiple generations

## File/Directory Issues

### Issue: "Permission denied" when saving

**Solutions**:
1. Check folder permissions
2. Run application from a folder you own
3. Create `generated_readers/` folder manually:
   ```bash
   mkdir generated_readers
   ```

### Issue: Generated files not found

**Check**:
1. `generated_readers/` folder exists
2. Files are in a timestamped subfolder
3. Path is printed in success message

## API Cost Issues

### Issue: Higher costs than expected

**Typical costs per reader**:
- Story: $0.05-0.15
- Images (8 pages): ~$0.32
- Total: ~$0.40-0.50

**Cost factors**:
1. Reading level (higher levels = longer stories)
2. Number of pages
3. Number of generation attempts
4. Image quality settings

**To reduce costs**:
1. Generate lower reading levels
2. Use fewer characters
3. Don't regenerate unnecessarily
4. Test with minimal inputs first

### Issue: API credits running out

**Solutions**:
1. Add payment method to your API account
2. Monitor usage in provider dashboards
3. Set up billing alerts
4. Use API key with proper rate limits

## Still Having Issues?

If none of these solutions work:

1. **Check the logs**: Look for error messages in the terminal
2. **Update dependencies**: `pip install --upgrade -r requirements.txt`
3. **Restart everything**: Close terminal, restart app
4. **Check API status pages**: Both Anthropic and OpenAI
5. **Try a minimal example**: Use all default settings
6. **Search for the error**: Copy exact error message to search engine
7. **Check versions**: Ensure Python 3.8+ and latest package versions

## Reporting Issues

When reporting issues, include:
- Python version (`python --version`)
- OS and version
- Full error message
- Steps to reproduce
- What you've already tried

## Getting Help

- 📖 Read the full [README.md](README.md)
- 🔍 Search existing GitHub issues
- 💬 Open a new GitHub issue with details
- 📧 Contact support (if applicable)

---

**Most issues are solved by**:
1. Checking API keys
2. Restarting the application
3. Reinstalling dependencies
4. Verifying internet connection
