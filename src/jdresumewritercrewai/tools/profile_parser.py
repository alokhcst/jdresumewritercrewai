from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json


class ParseProfileInput(BaseModel):
    """Input schema for CandidateProfileParser."""
    profile_data: str = Field(..., description="The candidate profile data (as JSON string or text)")


class CandidateProfileParser(BaseTool):
    name: str = "Parse Candidate Profile"
    description: str = (
        "Parses candidate profile data from JSON format and returns a structured, "
        "human-readable breakdown. Useful for organizing candidate information including "
        "personal details, work experience, skills, education, and achievements."
    )
    args_schema: Type[BaseModel] = ParseProfileInput

    def _run(self, profile_data: str) -> str:
        """Parse candidate profile data into structured format."""
        try:
            # Try to parse as JSON
            if isinstance(profile_data, str):
                profile = json.loads(profile_data)
            else:
                profile = profile_data
            
            # Build structured output
            output_parts = []
            
            # Personal Information
            if 'personal_info' in profile:
                output_parts.append("=== PERSONAL INFORMATION ===")
                for key, value in profile['personal_info'].items():
                    output_parts.append(f"{key.title()}: {value}")
                output_parts.append("")
            
            # Professional Summary
            if 'professional_summary' in profile:
                output_parts.append("=== PROFESSIONAL SUMMARY ===")
                output_parts.append(profile['professional_summary'])
                output_parts.append("")
            
            # Technical Skills
            if 'technical_skills' in profile:
                output_parts.append("=== TECHNICAL SKILLS ===")
                for category, skills in profile['technical_skills'].items():
                    if skills:
                        output_parts.append(f"{category.title()}: {', '.join(skills)}")
                output_parts.append("")
            
            # Work Experience
            if 'work_experience' in profile:
                output_parts.append("=== WORK EXPERIENCE ===")
                for idx, exp in enumerate(profile['work_experience'], 1):
                    output_parts.append(f"\nExperience {idx}:")
                    if 'title' in exp:
                        output_parts.append(f"  Title: {exp['title']}")
                    if 'company' in exp:
                        output_parts.append(f"  Company: {exp['company']}")
                    if 'duration' in exp:
                        output_parts.append(f"  Duration: {exp['duration']}")
                    if 'responsibilities' in exp and exp['responsibilities']:
                        output_parts.append("  Responsibilities:")
                        for resp in exp['responsibilities']:
                            output_parts.append(f"    - {resp}")
                    if 'achievements' in exp and exp['achievements']:
                        output_parts.append("  Achievements:")
                        for ach in exp['achievements']:
                            output_parts.append(f"    - {ach}")
                    if 'technologies' in exp and exp['technologies']:
                        output_parts.append(f"  Technologies: {', '.join(exp['technologies'])}")
                output_parts.append("")
            
            # Education
            if 'education' in profile and profile['education']:
                output_parts.append("=== EDUCATION ===")
                for edu in profile['education']:
                    output_parts.append(f"- {edu}")
                output_parts.append("")
            
            # Certifications
            if 'certifications' in profile and profile['certifications']:
                output_parts.append("=== CERTIFICATIONS ===")
                for cert in profile['certifications']:
                    output_parts.append(f"- {cert}")
                output_parts.append("")
            
            # Achievements
            if 'achievements' in profile and profile['achievements']:
                output_parts.append("=== ACHIEVEMENTS ===")
                for ach in profile['achievements']:
                    output_parts.append(f"- {ach}")
                output_parts.append("")
            
            # Volunteering
            if 'volunteering' in profile and profile['volunteering']:
                output_parts.append("=== VOLUNTEERING ===")
                for vol in profile['volunteering']:
                    output_parts.append(f"- {vol}")
                output_parts.append("")
            
            return '\n'.join(output_parts)
        
        except json.JSONDecodeError as e:
            return f"Error: Invalid JSON format - {str(e)}"
        except Exception as e:
            return f"Error parsing profile: {str(e)}"

