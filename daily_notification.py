import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from usaspending_api import get_contracts, save_contracts_to_excel
from ai_tools import predict_success_probability, summarize_contract, classify_probability, analyze_sentiment, opportunity_matching
from gpt_integration import generate_proposal_outline, generate_email_intro
from os.path import basename
from datetime import datetime

def send_email(subject, body, to_email, attachment=None):
    from_email = "plysius@zoeconn.com"
    password = "zConnor12$&"
    
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.attach(MIMEText(body, 'plain'))

    if attachment:
        with open(attachment, "rb") as f:
            part = MIMEApplication(f.read(), Name=basename(attachment))
        part['Content-Disposition'] = f'attachment; filename="{basename(attachment)}"'
        msg.attach(part)

    with smtplib.SMTP_SSL('smtp.example.com', 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

def job():
    contracts = get_contracts(1000000, 30, award_status='active', state='CA', county='001', naics='541511')  # Modify parameters as needed
    filename = f'contracts_{datetime.now().strftime("%Y-%m-%d")}.xlsx'
    save_contracts_to_excel(contracts, filename)

    # Generate email introduction drafts for each contract
    email_intros = []
    for contract in contracts:
        contract_details = contract['transaction_description']
        email_intro = generate_email_intro(contract_details)
        email_intros.append(email_intro)

    # Create email body
    body = "Daily contracts report attached.\n\nEmail Intros:\n" + "\n\n".join(email_intros)
    send_email("Daily Contracts Report", body, "plysius@zoeconn.com", filename)

schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
