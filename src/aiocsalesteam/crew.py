from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from aiocsalesteam.tools.tip_sender_tool import TipSenderTool
from aiocsalesteam.tools.set_greeting_tool import SetGreetingTool
from crewai_tools import EXASearchTool
from mem0 import MemoryClient


@CrewBase
class AIOCSalesTeam:
    """AIOCSalesTeam crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    client = MemoryClient()

    # Agent definitions
    @agent
    def prices_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['prices_expert'],
            tools=[EXASearchTool()],
            verbose=True
        )

    @agent
    def sales_rep_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['sales_rep_expert'],
            tools=[TipSenderTool(), SetGreetingTool()],  # Tool for sending NEAR Tokens as a tip
            verbose=True
        )

    @agent
    def sales_apprentice(self) -> Agent:
        return Agent(
            config=self.agents_config['sales_apprentice'],
            verbose=True
        )

    @task
    def looking_for_prices_task(self) -> Task:
        return Task(
            config=self.tasks_config['looking_for_prices_task'],
            tools=[EXASearchTool()]
        )

    @task
    def sales_teaching_task(self) -> Task:
        return Task(
            config=self.tasks_config['sales_teaching_task'],
        )

    @task
    def sales_pitch_task(self) -> Task:
        return Task(
            config=self.tasks_config['sales_pitch_task'],
            output_file='sales_pitch.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AIOCSalesTeam crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you want to use that instead
            # https://docs.crewai.com/how-to/Hierarchical/
            memory=True,
            memory_config={
                "provider": "mem0",
                "config": {"user_id": "Joe"},
            },
        )
