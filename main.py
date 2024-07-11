import schedule
import time
from usaspending_api import fetch_contracts
from nlp_analysis import analyze_opportunities
from gpt_analysis import analyze_opportunities_gpt4
from email_notifications import send_email

def job():
    opportunity_types = ["RFP", "RFI", "Sources Sought"]
    contracts_30_days = fetch_contracts(30, opportunity_types)
    analyzed_contracts_30_days = analyze_opportunities(contracts_30_days)
    analyzed_contracts_gpt4 = analyze_opportunities_gpt4(analyzed_contracts_30_days)
    # Convert DataFrame to a string or format as needed
    contracts_summary = analyzed_contracts_gpt4.to_string()
    send_email("Daily Contract Opportunities", contracts_summary, "recipient@example.com")

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

