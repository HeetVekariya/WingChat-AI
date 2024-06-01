from dotenv import load_dotenv
load_dotenv()   

from src.chatapp_crew.crew import HealthAdvisorCrew

def run():
    inputs = {
        'data': 'src\chatapp_crew\data\\blood_report.pdf',
    }
    HealthAdvisorCrew().health_advisor_crew().kickoff(inputs)

if __name__ == "__main__":
    run()