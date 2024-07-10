import requests
import json

# Base URL for the USASpending API
BASE_URL = 'https://api.usaspending.gov/api/v2'

# Define your agency and award details here
TOPTIER_AGENCY_CODE = '012'  # Example code
AWARD_ID = '123456'  # Example ID
BUREAU_SLUG = 'bureau_slug_example'  # Example slug

# Endpoints dictionary with method types and example payloads for POST requests
endpoints = {
    "agency": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/", "method": "GET"},
    "agency_awards": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/awards/", "method": "GET"},
    "agency_awards_new_count": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/awards/new/count/", "method": "GET"},
    "agency_awards_count": {"url": "/agency/awards/count/", "method": "GET"},
    "agency_budget_function": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/budget_function/", "method": "GET"},
    "agency_budget_function_count": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/budget_function/count/", "method": "GET"},
    "agency_budgetary_resources": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/budgetary_resources/", "method": "GET"},
    "agency_federal_account": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/federal_account/", "method": "GET"},
    "agency_federal_account_count": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/federal_account/count/", "method": "GET"},
    "agency_object_class": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/object_class/", "method": "GET"},
    "agency_object_class_count": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/object_class/count/", "method": "GET"},
    "agency_obligations_by_award_category": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/obligations_by_award_category/", "method": "GET"},
    "agency_program_activity": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/program_activity/", "method": "GET"},
    "agency_program_activity_count": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/program_activity/count/", "method": "GET"},
    "agency_sub_agency": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/sub_agency/", "method": "GET"},
    "agency_sub_agency_count": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/sub_agency/count/", "method": "GET"},
    "agency_sub_components_bureau": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/sub_components/{BUREAU_SLUG}/", "method": "GET"},
    "agency_sub_components": {"url": f"/agency/{TOPTIER_AGENCY_CODE}/sub_components/", "method": "GET"},
    "award_spending_recipient": {"url": "/award_spending/recipient/", "method": "GET"},
    "awards": {"url": f"/awards/{AWARD_ID}/", "method": "GET"},
    "awards_count_federal_account": {"url": f"/awards/count/federal_account/{AWARD_ID}/", "method": "GET"},
    "awards_count_subaward": {"url": f"/awards/count/subaward/{AWARD_ID}/", "method": "GET"},
    "awards_count_transaction": {"url": f"/awards/count/transaction/{AWARD_ID}/", "method": "GET"},
    "awards_funding_rollup": {"url": "/awards/funding_rollup/", "method": "GET"},
    "awards_last_updated": {"url": "/awards/last_updated/", "method": "GET"},
    "bulk_download_awards": {"url": "/bulk_download/awards/", "method": "GET"},
    "bulk_download_list_monthly_files": {"url": "/bulk_download/list_monthly_files/", "method": "GET"},
    "bulk_download_status": {"url": "/bulk_download/status/", "method": "GET"},
    "download_contract": {"url": "/download/contract/", "method": "GET"},
    "idvs_activity": {"url": "/idvs/activity/", "method": "GET"},
    "references_cfda_totals": {"url": "/references/cfda/totals/", "method": "GET"},
    "search_spending_by_transaction_grouped": {"url": "/search/spending_by_transaction_grouped/", "method": "POST", "payload": {
        "filters": {
            "time_period": [{"start_date": "2020-01-01", "end_date": "2020-12-31"}]
        },
        "fields": ["Award ID", "Recipient Name"],
        "page": 1,
        "limit": 10
    }},
    "search_transaction_spending_summary": {"url": "/search/transaction_spending_summary/", "method": "POST", "payload": {
        "filters": {
            "time_period": [{"start_date": "2020-01-01", "end_date": "2020-12-31"}]
        },
        "fields": ["Award ID", "Recipient Name"],
        "page": 1,
        "limit": 10
    }},
    "subawards": {"url": "/subawards/", "method": "POST", "payload": {
        "filters": {
            "time_period": [{"start_date": "2020-01-01", "end_date": "2020-12-31"}]
        },
        "fields": ["Sub-Award ID", "Sub-Award Amount"],
        "page": 1,
        "limit": 10
    }}
}

def fetch_data(endpoint, method, payload=None):
    url = f"{BASE_URL}{endpoint}"
    if method == "GET":
        response = requests.get(url)
    elif method == "POST":
        response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        try:
            return response.json()
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {url}")
            return None
    else:
        print(f"Request to {url} failed with status code {response.status_code}")
        return None

def main():
    for key, info in endpoints.items():
        print(f"Fetching data from {info['url']} using {info['method']} method...")
        data = fetch_data(info['url'], info['method'], info.get('payload'))
        if data:
            print(json.dumps(data, indent=4))
        else:
            print(f"No data returned for {info['url']}")

if __name__ == "__main__":
    main()


