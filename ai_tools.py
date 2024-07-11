from transformers import pipeline
from textblob import TextBlob

def predict_success_probability(text):
    classifier = pipeline('text-classification', model='your_chosen_model')
    results = classifier(text)
    return results

def summarize_contract(text):
    summarizer = pipeline('summarization', model='your_chosen_model')
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def classify_probability(score):
    if score > 0.75:
        return 'High'
    elif score > 0.5:
        return 'Medium'
    else:
        return 'Low'

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def opportunity_matching(contract_description, capabilities):
    return any(capability in contract_description for capability in capabilities)
