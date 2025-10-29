# Intelligent Resume Generator with CrewAI

An advanced multi-agent AI system powered by CrewAI that automatically generates tailored, ATS-optimized resumes based on job descriptions and candidate profiles.

## 🎯 Overview

This system uses 10 specialized AI agents that collaboratively analyze job postings, research companies, organize candidate profiles, match skills to requirements, write compelling content, and generate comprehensive job application packages including resumes, cover letters, skills gap analysis, interview preparation guides, and LinkedIn outreach messages.

## 🏗️ Architecture

### Agents
1. **Job Analyzer** - Extracts job requirements, skills, and ATS keywords
2. **Company Intelligence** - Researches company culture and tech stack
3. **Candidate Profiler** - Organizes candidate experience and skills
4. **Skills Matcher** - Matches skills to job requirements and ranks experiences
5. **Resume Writer** - Creates compelling, ATS-optimized content
6. **Formatter** - Assembles final markdown resume with QA
7. **Cover Letter Writer** - Creates personalized cover letters
8. **Skills Gap Analyzer** - Analyzes skill gaps and provides recommendations
9. **Interview Prep Specialist** - Generates interview questions and prep guides
10. **LinkedIn Message Writer** - Creates professional outreach messages

### Workflow
```
Job Posting → Job Analysis → Skills Matching → Content Creation → Resume.md
                    ↓                                   ↑
            Company Research                    Profile Organization
                    ↓
            Cover Letter Creation
                    ↓
            Skills Gap Analysis
                    ↓
            Interview Preparation
                    ↓
            LinkedIn Outreach Messages
```

## 🚀 Quick Start

1. **Install dependencies**:
```bash
pip install uv
crewai install
```

2. **Set up environment variables** in `.env`:
```bash
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key  # Optional
```

3. **Configure inputs** in `src/jdresumewritercrewai/main.py`:
   - Job posting URL or file path
   - Company name
   - Candidate profile (see `sample_candidate_profile.json`)

4. **Run the crew**:
```bash
crewai run
```

5. **Output**: Generated comprehensive job application package:
   - `resume.md` - ATS-optimized resume
   - `cover_letter.md` - Personalized cover letter
   - `skills_gap_analysis.md` - Skills gap analysis and recommendations
   - `interview_prep_guide.md` - Comprehensive interview preparation
   - `linkedin_messages.md` - LinkedIn outreach messages

## 📝 Input Format

### Candidate Profile (JSON)
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
  "technical_skills": {
    "languages": ["Python", "JavaScript"],
    "frameworks": ["React", "Django"],
    "databases": ["PostgreSQL", "MongoDB"],
    "cloud_platforms": ["AWS", "Docker"]
  },
  "work_experience": [
    {
      "company": "Tech Corp",
      "title": "Senior Engineer",
      "duration": "2020 - Present",
      "achievements": ["Improved performance by 40%"],
      "technologies": ["Python", "AWS"]
    }
  ],
  "education": ["BS Computer Science | University | 2020"],
  "certifications": ["AWS Certified | AWS | 2021"]
}
```

## 📄 Output

The system generates a comprehensive job application package:

### Core Documents
- **resume.md** - ATS-optimized resume with tailored content
- **cover_letter.md** - Personalized cover letter for the specific role

### Analysis & Preparation
- **skills_gap_analysis.md** - Detailed gap analysis with learning recommendations
- **interview_prep_guide.md** - Comprehensive interview questions and preparation strategies
- **linkedin_messages.md** - Professional outreach messages for hiring managers and recruiters

### Convert to PDF
```bash
python convert_all_to_html.py  # Convert all files to HTML
# Then open each .html file in browser and print to PDF
```

## 🛠️ Customization

- **Agents**: Edit `src/jdresumewritercrewai/config/agents.yaml`
- **Tasks**: Edit `src/jdresumewritercrewai/config/tasks.yaml`
- **Tools**: Add custom tools in `src/jdresumewritercrewai/tools/`

## 📚 Features

✅ **Multi-agent collaborative workflow** - 10 specialized AI agents  
✅ **ATS optimization** with keyword matching  
✅ **Company culture alignment** through research  
✅ **Skills gap analysis** with detailed recommendations  
✅ **Achievement-focused content** with metrics  
✅ **Cover letter generation** tailored to specific roles  
✅ **Interview preparation** with comprehensive guides  
✅ **LinkedIn outreach** messages for networking  
✅ **Markdown format** ready for PDF conversion  
✅ **Fully customizable** agent behaviors  

## 🆘 Support

- [CrewAI Documentation](https://docs.crewai.com)
- [GitHub Issues](https://github.com/joaomdmoura/crewai/issues)
- [Discord Community](https://discord.com/invite/X4JWnZnxPb)

---

Built with ❤️ using [CrewAI](https://crewai.com)

For detailed documentation, see [src/jdresumewritercrewai/README.md](src/jdresumewritercrewai/README.md)
