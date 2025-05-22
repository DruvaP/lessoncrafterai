from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from lessoncrafterai.tools.vectorize_pdf import VectorizePDFTool
from lessoncrafterai.tools.analyze_topics import AnalyzeTopicsTool
from lessoncrafterai.tools.generate_lessons import GenerateLessonsTool

@CrewBase
class LessonCrafterCrew:
    """LessonCrafter crew for curriculum ingestion and topic analysis"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def curriculum_ingestor(self) -> Agent:
        return Agent(
            config=self.agents_config['curriculum_ingestor'],
            tools=[VectorizePDFTool(
                pdf_path="knowledge/sample_curriculum.pdf",
                persist_dir="knowledge/vectorstore"
            )],
            verbose=True
        )

    @agent
    def topic_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config["topic_analyzer"],
            tools=[AnalyzeTopicsTool(persist_dir="knowledge/vectorstore")],
            verbose=True
        )

    @agent
    def lesson_planner(self) -> Agent:
        return Agent(
            config=self.agents_config["lesson_planner"],
            tools=[GenerateLessonsTool()],
            verbose=True
        )
   

    @task
    def vectorize_pdf_task(self) -> Task:
        return Task(
            config=self.tasks_config["vectorize_pdf_task"],
            agent=self.curriculum_ingestor()
        )

    @task
    def topic_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["topic_analysis_task"],
            agent=self.topic_analyzer()
        )
        
    @task
    def lesson_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config["lesson_planning_task"],
            agent=self.lesson_planner()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
