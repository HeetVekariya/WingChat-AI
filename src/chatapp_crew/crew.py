from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os
import yaml
from langchain_community.llms import HuggingFaceEndpoint

ollama_model = HuggingFaceEndpoint(
    # endpoint_url="https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct",
    endpoint_url="https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3",
    huggingfacehub_api_token=os.environ.get("HUGGINGFACE_API_TOKEN"),
    task="text-generation",
    max_new_tokens=2048
)

# Define your function to load YAML configuration
def load_config(yaml_file):
    with open(yaml_file, 'r') as file:
        return yaml.safe_load(file)
    
# Load the configuration
tasks_config = load_config('src/chatapp_crew/config/tasks.yaml')
agents_config = load_config('src/chatapp_crew/config/agents.yaml')

@CrewBase
class HealthAdvisorCrew():
    """Health Advisor Crew"""

    agents_config = 'config\\agents.yaml'
    tasks_config = 'config\\tasks.yaml'
    
    def __init__(self) -> None:
        self.llm = ollama_model

    @agent
    def report_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['report_analyst'],
            llm=self.llm
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            llm=self.llm
        )

    @agent
    def recommender(self) -> Agent:
        return Agent(
            config=self.agents_config['recommender'],
            llm=self.llm
        )

    @task
    def blood_report_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['blood_report_analysis_task'],
            agent=self.report_analyst(),
        )

    @task
    def article_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['articles_search_task'],
            agent=self.researcher(),
        )

    @task
    def recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config['recommendation_task'],
            agent=self.recommender(),
        )
    
    @crew
    def health_advisor_crew(self) -> Crew:
        return Crew(
            tasks=self.tasks,
            agents=self.agents,
            processes=Process.sequential,
            verbose=2,
            output_log_file='logs.txt'
        )