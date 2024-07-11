import pandas as pd
from datetime import datetime
from usaspending_api import get_contracts, save_contracts_to_excel

def get_micro_purchases(contracts, threshold=10000):
    micro_purchases = [contract for contract in contracts if contract['total_dollars_obligated'] <= threshold]
    return micro_purchases

def geographical_advantage_filter(contracts, preferred_state):
    geo_advantage_contracts = [contract for contract in contracts if contract['recipient_state_code'] == preferred_state]
    return geo_advantage_contracts

def get_renewal_opportunities(contracts, days_to_end=60):
    renewal_opportunities = []
    for contract in contracts:
        end_date = pd.to_datetime(contract['period_of_performance_potential_end_date'])
        if (end_date - pd.Timestamp.today()).days <= days_to_end:
            renewal_opportunities.append(contract)
    return renewal_opportunities

def contact_analysis(contracts):
    contacts = {}
    for contract in contracts:
        contact_name = contract['recipient_name']
        if contact_name in contacts:
            contacts[contact_name] += 1
        else:
            contacts[contact_name] = 1
    return contacts

def analyze_past_awards(contracts):
    past_awards = pd.DataFrame(contracts)
    award_trends = past_awards.groupby('recipient_name')['total_dollars_obligated'].sum().reset_index()
    return award_trends

def feedback_analysis(feedback_text):
    feedback_keywords = ["positive", "negative", "improvement", "strength"]
    feedback_scores = {keyword: feedback_text.lower().count(keyword) for keyword in feedback_keywords}
    return feedback_scores

def save_additional_analysis_to_excel(contracts):
    # Micro-Purchase Opportunities
    micro_purchases = get_micro_purchases(contracts)
    micro_purchases_df = pd.DataFrame(micro_purchases)

    # Geographical Advantage
    geo_advantage_contracts = geographical_advantage_filter(contracts, 'CA')
    geo_advantage_df = pd.DataFrame(geo_advantage_contracts)

    # Contract Renewal Opportunities
    renewal_opportunities = get_renewal_opportunities(contracts)
    renewal_opportunities_df = pd.DataFrame(renewal_opportunities)

    # Contact Analysis
    contacts = contact_analysis(contracts)
    contacts_df = pd.DataFrame(list(contacts.items()), columns=['Contact Name', 'Number of Contracts'])

    # Past Award Trends
    award_trends = analyze_past_awards(contracts)

    # Create an Excel writer object and save all dataframes
    filename = f'additional_analysis_{datetime.now().strftime("%Y-%m-%d")}.xlsx'
    with pd.ExcelWriter(filename) as writer:
        micro_purchases_df.to_excel(writer, sheet_name='Micro-Purchases', index=False)
        geo_advantage_df.to_excel(writer, sheet_name='Geographical Advantage', index=False)
        renewal_opportunities_df.to_excel(writer, sheet_name='Renewal Opportunities', index=False)
        contacts_df.to_excel(writer, sheet_name='Contact Analysis', index=False)
        award_trends.to_excel(writer, sheet_name='Past Award Trends', index=False)

    return filename

# Example usage
contracts = get_contracts(1000000, 30, award_status='active', state='CA', county='001', naics='541511')
additional_analysis_filename = save_additional_analysis_to_excel(contracts)
print(f'Saved additional analysis to {additional_analysis_filename}')
