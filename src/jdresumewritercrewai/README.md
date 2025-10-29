# Intelligent Resume Generator with CrewAI

An advanced multi-agent AI system powered by CrewAI that automatically generates tailored, ATS-optimized resumes based on job descriptions and candidate profiles.

## 🎯 Features

- **Multi-Agent Architecture**: Specialized AI agents work collaboratively to generate perfect resumes
- **Job Description Analysis**: Deep analysis of job postings to extract requirements, skills, and keywords
- **Company Intelligence**: Research company culture and values to tailor content appropriately
- **Skills Matching**: Intelligent matching of candidate skills to job requirements
- **ATS Optimization**: Content optimized for Applicant Tracking Systems
- **Markdown Format**: Clean markdown output ready for PDF conversion
- **Customizable**: Easily modify agent behaviors and workflows

## 🏗️ Architecture

The system consists of 6 specialized agents working in a sequential workflow:

### Agents

1. **Job Analyzer** - Extracts and analyzes job description details, required skills, and ATS keywords
2. **Company Intelligence** - Researches company culture, tech stack, and recent developments
3. **Candidate Profiler** - Organizes candidate experience, skills, and achievements
4. **Skills Matcher** - Matches candidate skills to job requirements and ranks experiences
5. **Resume Writer** - Creates compelling, ATS-optimized content with metrics and achievements
6. **Formatter** - Assembles final markdown resume with proper structure and QA

### Workflow

```
Job Posting → Job Analysis → Skills Matching → Content Creation → Resume Assembly
                    ↓                                   ↑
            Company Research                    Profile Organization
```

## 📋 Prerequisites

- Python >=3.10 <3.14
- UV package manager (recommended)
- OpenAI API key
- Serper API key (optional, for company research)

## 🚀 Installation

1. **Install UV** (if not already installed):
```bash
pip install uv
```

2. **Install dependencies**:
```bash
crewai install
```

3. **Set up environment variables**:
Create a `.env` file in the project root:
```bash
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key  # Optional, for company research
```

## 📝 Input Format

### Job Description
Provide either:
- A URL to the job posting (will be scraped automatically)
- A local file path with job description text
- Plain text in the input

### Candidate Profile
Provide candidate information in JSON format:

```json
{
  "personal_info": {
    "name": "John Doe",
    "email": "john.doe@email.com",
    "phone": "+1-555-123-4567",
    "linkedin": "linkedin.com/in/johndoe",
    "github": "github.com/johndoe",
    "location": "San Francisco, CA"
  },
  "professional_summary": "Your current summary...",
  "technical_skills": {
    "languages": ["Python", "JavaScript", "Java"],
    "frameworks": ["React", "Django", "Flask"],
    "databases": ["PostgreSQL", "MongoDB", "Redis"],
    "cloud_platforms": ["AWS", "GCP", "Docker", "Kubernetes"],
    "tools": ["Git", "Jenkins", "JIRA"],
    "methodologies": ["Agile", "Scrum", "CI/CD"]
  },
  "work_experience": [
    {
      "company": "Tech Corp Inc",
      "title": "Senior Software Engineer",
      "duration": "January 2020 - Present",
      "responsibilities": ["Lead development..."],
      "achievements": ["Improved performance by 40%..."],
      "technologies": ["Python", "Django", "AWS"]
    }
  ],
  "education": ["Degree | University | Year"],
  "certifications": ["Cert Name | Issuer | Year"],
  "achievements": ["Notable achievement..."],
  "volunteering": ["Organization | Role | Period"]
}
```

See `sample_candidate_profile.json` for a complete example.

## 🎮 Usage

### Basic Usage

1. **Edit the inputs** in `src/jdresumewritercrewai/main.py`:
```python
job_posting_url = "https://example.com/job-posting"  # Or local file path
company_name = "Company Name"
candidate_profile = {...}  # Your candidate data
```

2. **Run the crew**:
```bash
crewai run
```

### Advanced Usage

#### Load Profile from File
```python
import json

with open('sample_candidate_profile.json', 'r') as f:
    candidate_profile = json.load(f)

inputs = {
    'job_posting_url': 'path/to/job_description.txt',
    'company_name': 'Target Company',
    'candidate_profile': json.dumps(candidate_profile)
}

result = Jdresumewritercrewai().crew().kickoff(inputs=inputs)
```

#### Using Job Description from File
Create a file `knowledge/job_description.txt` with the job posting text and reference it:
```python
job_posting_url = "knowledge/job_description.txt"
```

## 📄 Output

The crew generates a `resume.md` file in the project root with:

- Contact information header
- Tailored professional summary
- Certifications (if applicable)
- Achievements (if applicable)
- Technical skills section
- Professional experience with achievement-focused bullets
- Education
- Volunteering activities (if applicable)

### Converting to PDF

You can convert the markdown to PDF using various tools:

**Option 1: Using Pandoc**
```bash
pandoc resume.md -o resume.pdf --pdf-engine=xelatex
```

**Option 2: Using Python (markdown + weasyprint)**
```python
import markdown2
from weasyprint import HTML

with open('resume.md', 'r') as f:
    html = markdown2.markdown(f.read())
    HTML(string=html).write_pdf('resume.pdf')
```

**Option 3: Using Grip (GitHub-style)**
```bash
grip resume.md --export resume.html
# Then convert HTML to PDF using any HTML to PDF tool
```

## 🛠️ Customization

### Modifying Agents

Edit `src/jdresumewritercrewai/config/agents.yaml` to change agent roles, goals, or backstories.

### Modifying Tasks

Edit `src/jdresumewritercrewai/config/tasks.yaml` to adjust task descriptions, expected outputs, or dependencies.

### Adding Tools

Create new tools in `src/jdresumewritercrewai/tools/` and add them to agents in `crew.py`.

Example: Adding a LinkedIn research tool

1. Create `tools/linkedin_research.py`:
```python
from crewai.tools import BaseTool
# ... implement tool
```

2. Import and add to agent in `crew.py`:
```python
from tools.linkedin_research import LinkedInResearchTool

@agent
def company_intelligence(self) -> Agent:
    return Agent(
        config=self.agents_config['company_intelligence'],
        tools=[SerperDevTool(), ScrapeWebsiteTool(), LinkedInResearchTool()]
    )
```

## 🧪 Testing

Test the crew execution:
```bash
crewai test
```

Train the crew (improves performance over iterations):
```bash
crewai train
```

## 📚 Key Considerations

### ATS Optimization
- Uses standard section headers
- Avoids tables and complex formatting
- Natural keyword incorporation
- Quantifiable achievements focus

### Skills Matching
- Ranks experiences by job relevance
- Highlights strong skill matches
- Identifies potential skill gaps

### Content Quality
- Achievement-focused bullet points with metrics
- Professional, clear writing style
- Company culture alignment
- Keyword-rich without being obvious

## 🚧 Advanced Features

Consider implementing:
- Multiple resume versions for different roles
- Cover letter generation
- Skills gap analysis
- Interview preparation based on company research
- Automated job application tracking

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support, questions, or feedback:
- Visit [CrewAI Documentation](https://docs.crewai.com)
- Check [GitHub Issues](https://github.com/joaomdmoura/crewai/issues)
- Join [Discord Community](https://discord.com/invite/X4JWnZnxPb)

---

Built with ❤️ using [CrewAI](https://crewai.com)

