# Quick Start Guide - Resume Generation System

## 🚀 Generate Complete Job Application Package

### Step 1: Configure Your Inputs

Edit these files in the `input/` folder:
- **`input/job_url.txt`** - Paste the job posting URL
- **`input/company_name.txt`** - Enter the company name
- **`input/sample_candidate_profile.json`** - Update with your information
- **`input/job_description.txt`** - (Optional) Paste job description text

### Step 2: Run the Crew

```bash
crewai run
```

This generates 10 files in the `output/` directory:
- ✅ `output/resume.md` - Your tailored resume
- ✅ `output/cover_letter.md` - Personalized cover letter
- ✅ `output/skills_gap_analysis.md` - Skills analysis with learning plan
- ✅ `output/interview_prep_guide.md` - Interview questions & prep
- ✅ `output/linkedin_messages.md` - LinkedIn outreach messages
- ✅ `output/proposed_job_analysis.md` - Job requirements analysis
- ✅ `output/company_intelligence.md` - Company research
- ✅ `output/candidate_profile_analysis.md` - Your profile breakdown
- ✅ `output/skills_matching_report.md` - Skills matching analysis
- ✅ `output/resume_content.md` - Tailored content

### Step 3: Convert to PDF

```bash
python convert_all_to_html.py
```

This creates HTML versions of all files.

### Step 4: Print to PDF

1. Open any `.html` file in your browser
2. Press `Ctrl+P` (Windows) or `Cmd+P` (Mac)
3. Select "Save as PDF"
4. Click "Save"

## 📝 Key Files to Use

### For Job Application:
- `output/resume.md` / `output/resume.html` → Convert to PDF and submit
- `output/cover_letter.md` → Customize and submit with application

### For Interview Prep:
- `output/interview_prep_guide.md` → Study before interviews
- `output/skills_gap_analysis.md` → Plan your skill development

### For Networking:
- `output/linkedin_messages.md` → Copy messages for LinkedIn outreach

## 🔧 Common Commands

### Run the system:
```bash
crewai run
```

### Convert to HTML:
```bash
python convert_all_to_html.py
```

### Open resume in browser:
```bash
start output/resume.html             # Windows
open output/resume.html              # Mac
xdg-open output/resume.html          # Linux
```

## 🎯 What Each Output Contains

| File | Contents |
|------|----------|
| **output/resume.md** | Complete ATS-optimized resume |
| **output/cover_letter.md** | Personalized cover letter for the role |
| **output/skills_gap_analysis.md** | Skills you need to learn + resources |
| **output/interview_prep_guide.md** | Questions you'll be asked + how to answer |
| **output/linkedin_messages.md** | Messages for hiring managers & recruiters |

## 💡 Tips

1. **Review before submitting**: AI-generated content needs your review
2. **Customize**: Add personal touches to the cover letter
3. **Practice**: Use the interview guide to prepare answers
4. **Network**: Send LinkedIn messages within 24 hours of applying
5. **Skill up**: Follow the learning plan in skills_gap_analysis.md

## 🔄 For Multiple Jobs

1. Update `input/job_url.txt` with new job URL
2. Update `input/company_name.txt` with new company
3. Run `crewai run` again
4. Files will be regenerated for the new job

## ⚙️ Customize Agents

Edit these files to change how agents work:
- `src/jdresumewritercrewai/config/agents.yaml` - Agent behaviors
- `src/jdresumewritercrewai/config/tasks.yaml` - Task descriptions

## 📂 Output Directory Structure

```
jdresumewritercrewai/
├── input/
│   ├── job_url.txt                   # Input: Job URL
│   ├── company_name.txt              # Input: Company name
│   ├── job_description.txt           # Input: Job description (optional)
│   └── sample_candidate_profile.json # Input: Your profile
├── knowledge/
│   └── user_preference.txt           # System preferences
└── output/
    ├── resume.md                     # Main resume
    ├── resume.html                   # HTML version
    ├── cover_letter.md               # Cover letter
    ├── skills_gap_analysis.md        # Skills analysis
    ├── interview_prep_guide.md       # Interview prep
    ├── linkedin_messages.md          # LinkedIn messages
    ├── proposed_job_analysis.md      # Job analysis
    ├── company_intelligence.md       # Company research
    ├── candidate_profile_analysis.md # Your profile
    ├── skills_matching_report.md     # Skills matching
    └── resume_content.md             # Resume content
```

## 🆘 Troubleshooting

### "Module not found: markdown2"
```bash
pip install markdown2
```

### "Cannot run crewai"
```bash
pip install uv
crewai install
```

### Files not generating
Check that:
1. `input/job_url.txt` has a valid URL
2. `input/company_name.txt` has a company name
3. `input/sample_candidate_profile.json` is properly formatted

### Tool validation errors
The system will retry automatically. Check the terminal output for specific errors.

## 📧 Need Help?

- [CrewAI Documentation](https://docs.crewai.com)
- [Project README](README.md)
- [Setup Guide](SETUP_GUIDE.md)
- [Architecture Documentation](ARCHITECTURE.md)

---

**Ready to apply for your next role!** 🎉

