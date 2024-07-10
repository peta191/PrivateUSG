from transformers import pipeline

def analyze_opportunities(data):
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    classifier = pipeline("sentiment-analysis", model=model_name)
    
    data['Opportunity Score'] = data['Opportunity Description'].apply(lambda x: classifier(x)[0]['score'])
    return data

# Example usage
# contracts should have a column "Opportunity Description"
# analyzed_contracts = analyze_opportunities(contracts)

