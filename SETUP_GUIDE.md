# Setup Guide

## Prerequisites

- Python 3.10 - 3.13
- pip or uv package manager
- OpenAI API key
- (Optional) Serper API key for enhanced company research

## Installation Steps

### 1. Install Dependencies

Using UV (recommended):
```bash
pip install uv
crewai install
```

Or using pip:
```bash
pip install -e .
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional - for company research
SERPER_API_KEY=your_serper_api_key_here

# Optional - for verbose logging
VERBOSE=true
```

Get your API keys:
- OpenAI: https://platform.openai.com/api-keys
- Serper: https://serper.dev

### 3. Configure Your Inputs

Edit `src/jdresumewritercrewai/main.py`:

#### Option A: Use Example Data
Keep the default example data in the file.

#### Option B: Load from Files
```python
import json

# Load candidate profile from JSON
with open('sample_candidate_profile.json', 'r') as f:
    candidate_profile = json.load(f)

# Set job description file
job_posting_url = "knowledge/job_description.txt"
company_name = "Your Target Company"

inputs = {
    'job_posting_url': job_posting_url,
    'company_name': company_name,
    'candidate_profile': json.dumps(candidate_profile)
}
```

### 4. Provide Job Description

**Option A: From URL**
```python
job_posting_url = "https://example.com/job-posting-url"
```

**Option B: From Local File**
- Create `knowledge/job_description.txt` with the job posting text
```python
job_posting_url = "knowledge/job_description.txt"
```

**Option C: Plain Text**
- You can also modify the FileReadTool to handle raw text

### 5. Provide Candidate Profile

**Option A: Use Sample Profile**
- Use `sample_candidate_profile.json` as reference
- Replace with your actual data

**Option B: Create Custom Profile**
- Follow the JSON structure in `sample_candidate_profile.json`
- Include all required fields: personal_info, technical_skills, work_experience, etc.

## Running the System

### Basic Run
```bash
crewai run
```

### With Custom Inputs
```python
python -m jdresumewritercrewai.main
```

### Training Mode (for improvement)
```bash
crewai train <iterations> <filename>
```

### Test Mode
```bash
crewai test <iterations> <eval_llm>
```

## Output

The system generates `resume.md` in the project root with:
- Contact information
- Professional summary
- Skills sections
- Work experience
- Education
- Certifications
- Achievements

## Converting to PDF

### Using Pandoc
```bash
pandoc resume.md -o resume.pdf --pdf-engine=xelatex
```

### Using Python
```bash
pip install markdown2 weasyprint
python convert_to_pdf.py
```

Create `convert_to_pdf.py`:
```python
import markdown2
from weasyprint import HTML

with open('resume.md', 'r') as f:
    html_content = markdown2.markdown(f.read())

HTML(string=html_content).write_pdf('resume.pdf')
```

## Troubleshooting

### Error: ModuleNotFoundError
```bash
pip install --upgrade -e .
```

### Error: API Key not found
- Check `.env` file exists in project root
- Verify API key format (no quotes, no spaces)
- Restart your terminal

### Error: Cannot scrape URL
- Check internet connection
- Verify URL is accessible
- Use file-based job description instead

### Error: Invalid JSON
- Validate JSON syntax
- Check for trailing commas
- Use a JSON validator

### Poor Resume Quality
- Ensure detailed candidate profile
- Provide comprehensive job description
- Adjust agent backstories in `config/agents.yaml`

## Advanced Configuration

### Modify Agent Behavior
Edit `src/jdresumewritercrewai/config/agents.yaml`

### Modify Task Workflow
Edit `src/jdresumewritercrewai/config/tasks.yaml`

### Add Custom Tools
1. Create in `src/jdresumewritercrewai/tools/`
2. Import in `crew.py`
3. Assign to agents

### Change Output Format
Modify the `resume_assembly_task` in `config/tasks.yaml`

## Tips for Best Results

1. **Detailed Profiles**: More information = better matching
2. **Quantifiable Achievements**: Use numbers and metrics
3. **Comprehensive Skills**: List all technologies and tools
4. **Job Description Quality**: Full job posting yields better analysis
5. **Update Profiles**: Keep candidate data current
6. **Test Multiple JDs**: Try different job postings to see variations

## Next Steps

- Review generated `resume.md`
- Convert to PDF
- Customize agents for your domain
- Add more tools for enhanced research
- Implement batch processing for multiple resumes

## Support

For issues or questions:
- Check README.md
- Review ARCHITECTURE.md
- Open an issue on GitHub
- Visit CrewAI documentation

