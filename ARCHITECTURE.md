# Architecture Documentation

## System Overview

The Intelligent Resume Generator uses CrewAI's multi-agent architecture to create tailored, ATS-optimized resumes. The system consists of 6 specialized agents that work collaboratively in a sequential workflow.

## Agent Descriptions

### 1. Job Analyzer Agent
**Role**: Job Description Analyzer  
**Purpose**: Extracts and analyzes job posting details  
**Tools**: ScrapeWebsiteTool, FileReadTool  
**Key Responsibilities**:
- Parse job descriptions from URLs or files
- Extract required technical skills
- Identify soft skills and qualifications
- Extract ATS keywords
- Determine experience level requirements
- Document education requirements

**Output**: Structured job requirements and ATS keywords

### 2. Company Intelligence Agent
**Role**: Company Intelligence Researcher  
**Purpose**: Researches company culture and values  
**Tools**: SerperDevTool (web search), ScrapeWebsiteTool  
**Key Responsibilities**:
- Research company culture and values
- Find recent news, funding, or acquisitions
- Identify technology stack
- Research leadership team
- Understand products and services
- Analyze industry position

**Output**: Company intelligence report

### 3. Candidate Profiler Agent
**Role**: Candidate Profile Organizer  
**Purpose**: Organizes candidate data  
**Tools**: FileReadTool, CandidateProfileParser  
**Key Responsibilities**:
- Parse candidate profile JSON
- Organize personal information
- Catalog technical skills by category
- Structure work experience
- Organize education and certifications
- Compile achievements and volunteering

**Output**: Well-organized candidate profile

### 4. Skills Matcher Agent
**Role**: Skills and Experience Matcher  
**Purpose**: Matches candidate to job requirements  
**Key Responsibilities**:
- Compare candidate skills vs. required skills
- Rank work experiences by relevance
- Identify skill gaps
- Match achievements to job requirements
- Recommend experience ordering

**Output**: Skills matching report with ranked experiences

### 5. Resume Writer Agent
**Role**: Senior Resume Writer  
**Purpose**: Creates compelling resume content  
**Key Responsibilities**:
- Write tailored professional summary
- Create achievement-focused bullet points
- Incorporate metrics and quantifiable results
- Integrate ATS keywords naturally
- Align content with company culture
- Write skills sections

**Output**: Tailored resume content optimized for ATS

### 6. Formatter Agent
**Role**: Resume Formatter and QA Specialist  
**Purpose**: Assembles final markdown resume  
**Key Responsibilities**:
- Assemble all sections in markdown format
- Ensure ATS-friendly formatting
- Verify proper structure
- Check for formatting errors
- Ensure keyword placement
- Quality assurance

**Output**: Complete markdown resume (resume.md)

## Workflow

```
┌─────────────────┐
│  Job Posting    │
│  (URL/File)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Job Analyzer   │ → Job Requirements & ATS Keywords
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌─────────┐  ┌──────────────────────┐
│ Company │  │  Candidate Profiler  │
│Intel    │  │  (runs in parallel)  │
└────┬────┘  └──────────┬───────────┘
     │                  │
     └────────┬─────────┘
              │
              ▼
      ┌──────────────┐
      │Skills Matcher│ → Ranked Experiences & Matches
      └──────┬───────┘
             │
             ▼
      ┌──────────────┐
      │Resume Writer │ → Tailored Content
      └──────┬───────┘
             │
             ▼
        ┌─────────┐
        │Formatter│ → resume.md
        └─────────┘
```

## Data Flow

### Input
1. **Job Posting**: URL or file path containing job description
2. **Company Name**: Target company name
3. **Candidate Profile**: JSON structure with complete candidate information

### Processing
1. **Job Analysis**: Extract requirements, skills, keywords
2. **Company Research**: Gather intelligence on company
3. **Profile Organization**: Structure candidate data
4. **Skills Matching**: Match and rank experiences
5. **Content Creation**: Generate tailored content
6. **Resume Assembly**: Format final document

### Output
- **resume.md**: Markdown resume file ready for PDF conversion

## Key Design Decisions

### 1. Sequential Process
Tasks are executed in sequence to ensure proper data flow and dependencies.

### 2. Specialized Agents
Each agent has a focused role to maintain high quality outputs.

### 3. Tool Integration
Agents use appropriate tools for their specific tasks (scraping, file reading, web search).

### 4. ATS Optimization
All content is optimized for Applicant Tracking Systems with proper keywords and formatting.

### 5. Markdown Output
Markdown format ensures easy conversion to PDF while maintaining structure.

## Customization Points

### Agents
Modify `config/agents.yaml` to change:
- Role descriptions
- Goals
- Backstories
- Behavior

### Tasks
Modify `config/tasks.yaml` to change:
- Task descriptions
- Expected outputs
- Dependencies
- Agent assignments

### Tools
Add custom tools in `tools/` directory:
- Create new tool classes
- Implement _run methods
- Add to appropriate agents in crew.py

### Workflow
Change process type in crew.py:
- Sequential (current)
- Hierarchical
- Consensus

## Extensibility

### Adding New Agents
1. Add agent definition to `config/agents.yaml`
2. Add agent method to `crew.py`
3. Add corresponding tasks if needed

### Adding New Tools
1. Create tool class in `tools/`
2. Add to `tools/__init__.py`
3. Import and assign to agents in `crew.py`

### Adding New Tasks
1. Add task definition to `config/tasks.yaml`
2. Add task method to `crew.py`
3. Update dependencies if needed

## Performance Considerations

- Sequential processing ensures quality over speed
- File I/O operations for large profiles
- Web scraping rate limits may apply
- LLM API rate limits and costs
- Consider caching for repeated runs

## Error Handling

- File not found: Graceful error messages
- Network errors: Retry logic for scraping
- Invalid JSON: Clear error reporting
- Missing fields: Default values where appropriate

## Future Enhancements

1. **Batch Processing**: Generate multiple resume versions
2. **Cover Letter Generation**: Add cover letter agent
3. **Skills Gap Analysis**: Detailed gap reporting
4. **Interview Prep**: Generate interview questions
5. **Tracking**: Track application status
6. **Templates**: Multiple resume templates
7. **Web UI**: Browser-based interface

