from dotenv import load_dotenv
load_dotenv()   

from src.chatapp_crew.crew import HealthAdvisorCrew

def run():
    inputs = {
        'data': 'src\chatapp_crew\data\\blood_report.pdf',
        'search_tool': 'src\chatapp_crew\\tools\search_tool.py',
        'pdf_tool': 'src\chatapp_crew\\tools\pdf_tool.py',
    }
    HealthAdvisorCrew().health_advisor_crew().kickoff(inputs)

if __name__ == "__main__":
    run()