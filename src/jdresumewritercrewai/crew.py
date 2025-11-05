from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from jdresumewritercrewai.tools import ScrapeWebsiteTool, FileReadTool, CandidateProfileParser
from crewai_tools import SerperDevTool

@CrewBase
class Jdresumewritercrewai():
    """Resume Writer Crew - Intelligent Resume Generation using CrewAI"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def job_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['job_analyzer'], # type: ignore[index]
            tools=[ScrapeWebsiteTool(), FileReadTool()],
            verbose=True
        )

    @agent
    def company_intelligence(self) -> Agent:
        return Agent(
            config=self.agents_config['company_intelligence'], # type: ignore[index]
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def candidate_profiler(self) -> Agent:
        return Agent(
            config=self.agents_config['candidate_profiler'], # type: ignore[index]
            tools=[FileReadTool()],
            verbose=True
        )

    @agent
    def skills_matcher(self) -> Agent:
        return Agent(
            config=self.agents_config['skills_matcher'], # type: ignore[index]
            verbose=True
        )

    @agent
    def resume_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_writer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def formatter(self) -> Agent:
        return Agent(
            config=self.agents_config['formatter'], # type: ignore[index]
            verbose=True
        )

    @agent
    def cover_letter_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['cover_letter_writer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def skills_gap_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['skills_gap_analyzer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def interview_prep_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['interview_prep_specialist'], # type: ignore[index]
            verbose=True
        )

    @agent
    def linkedin_message_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['linkedin_message_writer'], # type: ignore[index]
            verbose=True
        )

    @task
    def job_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_research_task'], # type: ignore[index]
        )

    @task
    def company_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['company_research_task'], # type: ignore[index]
        )

    @task
    def candidate_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['candidate_analysis_task'], # type: ignore[index]
        )

    @task
    def skills_matching_task(self) -> Task:
        return Task(
            config=self.tasks_config['skills_matching_task'], # type: ignore[index]
        )

    @task
    def content_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_creation_task'], # type: ignore[index]
        )

    @task
    def resume_assembly_task(self) -> Task:
        return Task(
            config=self.tasks_config['resume_assembly_task'], # type: ignore[index]
        )

    @task
    def cover_letter_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['cover_letter_creation_task'], # type: ignore[index]
        )

    @task
    def skills_gap_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['skills_gap_analysis_task'], # type: ignore[index]
        )

    @task
    def interview_preparation_task(self) -> Task:
        return Task(
            config=self.tasks_config['interview_preparation_task'], # type: ignore[index]
        )

    @task
    def linkedin_outreach_task(self) -> Task:
        return Task(
            config=self.tasks_config['linkedin_outreach_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Resume Writer Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
