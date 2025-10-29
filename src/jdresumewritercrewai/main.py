#!/usr/bin/env python
import sys
import warnings
import json
import os

from datetime import datetime

from jdresumewritercrewai.crew import Jdresumewritercrewai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def read_file_content(file_path):
    """Helper function to read file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Warning: File {file_path} not found. Using default value.")
        return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def run():
    """
    Run the crew for resume generation.
    
    This function demonstrates how to use the resume generation crew.
    You can modify the inputs below or pass them via command line arguments.
    """
    
    # Read job posting URL from file, fallback to default
    job_posting_url = read_file_content("knowledge/job_url.txt") #or "https://example.com/job-posting-url"
    
    # Read company name from file, fallback to default
    company_name = read_file_content("knowledge/company_name.txt") #or "Example Company"
    
    # Load candidate profile from JSON file
    candidate_profile_path = "sample_candidate_profile.json"
    try:
        with open(candidate_profile_path, 'r', encoding='utf-8') as f:
            candidate_profile = json.load(f)
        print(f"✓ Loaded candidate profile from {candidate_profile_path}")
    except FileNotFoundError:
        print(f"Warning: {candidate_profile_path} not found. Using default profile.")
        # Fallback candidate profile
        candidate_profile = {
        "personal_info": {
            "name": "John Doe",
            "email": "john.doe@email.com",
            "phone": "+1-555-123-4567",
            "linkedin": "linkedin.com/in/johndoe",
            "github": "github.com/johndoe",
            "location": "San Francisco, CA"
        },
        "professional_summary": "Experienced software engineer with 8+ years in full-stack development.",
        "technical_skills": {
            "languages": ["Python", "JavaScript", "Java", "Go"],
            "frameworks": ["React", "Django", "Flask", "Express.js"],
            "databases": ["PostgreSQL", "MongoDB", "Redis"],
            "cloud_platforms": ["AWS", "GCP", "Docker", "Kubernetes"],
            "tools": ["Git", "Jenkins", "JIRA", "Confluence"],
            "methodologies": ["Agile", "Scrum", "CI/CD", "TDD"]
        },
        "work_experience": [
            {
                "company": "Tech Corp Inc",
                "title": "Senior Software Engineer",
                "duration": "January 2020 - Present",
                "responsibilities": [
                    "Lead development of microservices architecture",
                    "Mentor junior developers",
                    "Design and implement RESTful APIs"
                ],
                "achievements": [
                    "Improved system performance by 40% through optimization",
                    "Led team of 5 developers on critical projects",
                    "Reduced deployment time by 50% using CI/CD"
                ],
                "technologies": ["Python", "Django", "PostgreSQL", "AWS", "Docker"]
            },
            {
                "company": "StartupXYZ",
                "title": "Full Stack Developer",
                "duration": "June 2017 - December 2019",
                "responsibilities": [
                    "Developed frontend and backend features",
                    "Implemented authentication systems",
                    "Worked with cross-functional teams"
                ],
                "achievements": [
                    "Delivered 3 major product features on time",
                    "Increased user engagement by 25%",
                    "Implemented automated testing reducing bugs by 30%"
                ],
                "technologies": ["React", "Node.js", "MongoDB", "AWS"]
            }
        ],
        "education": [
            "Bachelor of Science in Computer Science | University of California | 2017"
        ],
        "certifications": [
            "AWS Certified Solutions Architect - Associate | AWS | 2021",
            "Certified Kubernetes Administrator | CNCF | 2022"
        ],
        "achievements": [
            "Best Innovation Award - Tech Corp Inc 2022",
            "Published 3 technical articles on medium.com"
        ],
        "volunteering": [
            "Code for America - Volunteer Software Developer | 2019-2020"
        ]
    }
    except Exception as e:
        print(f"Error loading candidate profile: {e}")
        raise
    
    # Print inputs being used
    print("\n" + "="*50)
    print("RESUME GENERATION INPUTS")
    print("="*50)
    print(f"Job Posting URL: {job_posting_url}")
    print(f"Company Name: {company_name}")
    print(f"Candidate: {candidate_profile.get('personal_info', {}).get('name', 'N/A')}")
    print("="*50 + "\n")
    
    inputs = {
        'job_posting_url': job_posting_url,
        'company_name': company_name,
        'candidate_profile': json.dumps(candidate_profile)
    }

    try:
        result = Jdresumewritercrewai().crew().kickoff(inputs=inputs)
        print("\n" + "="*60)
        print("COMPREHENSIVE JOB APPLICATION PACKAGE COMPLETE!")
        print("="*60)
        print("\nGenerated files:")
        print("📄 resume.md - ATS-optimized resume")
        print("📝 cover_letter.md - Personalized cover letter")
        print("📊 skills_gap_analysis.md - Skills gap analysis and recommendations")
        print("🎯 interview_prep_guide.md - Comprehensive interview preparation")
        print("💼 linkedin_messages.md - LinkedIn outreach messages")
        print("\nTo convert to PDF:")
        print("1. Run: python convert_to_html.py")
        print("2. Open resume.html in browser and print to PDF")
        print("3. Repeat for other .md files as needed")
        print("\n" + "="*60)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        Jdresumewritercrewai().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Jdresumewritercrewai().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        Jdresumewritercrewai().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": ""
    }

    try:
        result = Jdresumewritercrewai().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
