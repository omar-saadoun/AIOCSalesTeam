from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
from aiocsalesteam.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool


@CrewBase
class AIOCSalesTeam():
	"""AIOCsalesteam crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def sales_rep_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['sales_rep_expert'],
		    tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def sales_apprentice(self) -> Agent:
		return Agent(
			config=self.agents_config['sales_apprentice'],
			verbose=True
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
		"""Creates the AIOCsalesteam crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)