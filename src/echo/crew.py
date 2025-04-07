# src/latest_ai_development/crew.py
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource


@CrewBase
class Echo():
  """LatestAiDevelopment crew"""

  @agent
  def long_time_resident(self) -> Agent:
    return Agent(
      config=self.agents_config['long_time_resident'],
      verbose=True
    )

  @agent
  def young_family_resident(self) -> Agent:
    return Agent(
      config=self.agents_config['young_family_resident'],
      verbose=True
    ) 
  
  @task
  def long_time_resident_task_1(self) -> Task:
    return Task(
      config=self.tasks_config['long_time_resident_task_1'],
    )

  @task
  def young_family_task_1(self) -> Task:
    return Task(
      config=self.tasks_config['young_family_task_1'],
    )  

  @task
  def long_time_resident_task_2(self) -> Task:
    return Task(
      config=self.tasks_config['long_time_resident_task_2'],
    ) 

  @task
  def young_family_task_2(self) -> Task:
    return Task(
      config=self.tasks_config['young_family_task_2'],
    ) 

  @task
  def long_time_resident_task_3(self) -> Task:
    return Task(
      config=self.tasks_config['long_time_resident_task_3'],
    )  

  @task
  def young_family_task_3(self) -> Task:
    return Task(
      config=self.tasks_config['young_family_task_3'],
    )  

  @crew
  def crew(self) -> Crew:
    """Creates the LatestAiDevelopment crew"""

    pdf_paths=[
      "Green Belt Assessment Part 1 2015.pdf", 
      "Local Plan Policy 2017-2018.pdf","NPPF_December_2024.pdf",
      "Tandridge Core Strategy.pdf", 
      "Tandridge Economic Needs Assessment Update 2017.pdf",
      "Tandridge local plan policies.pdf", 
      "Tandridge Retail Leisure Study Update 2018.pdf"
    ]
    PDF_ks = PDFKnowledgeSource(file_paths=pdf_paths)

    txt_paths=[
      'newspaper_article.txt'
    ]

    TXT_ks = TextFileKnowledgeSource(file_paths=txt_paths)

    llm = LLM(
    model="openai/gpt-4", # call model by provider/model_name
    temperature=0.1,
    )

    return Crew(
      agents=self.agents, # Automatically created by the @agent decorator
      tasks=self.tasks, # Automatically created by the @task decorator
      process=Process.sequential,
      verbose=True,
      llm=llm,
      knowledge_sources = [PDF_ks,TXT_ks]
    )