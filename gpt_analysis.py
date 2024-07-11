import openai

def gpt4_analyze_opportunity(description):
    openai.api_key = 'your_openai_api_key'
    response = openai.Completion.create(
      engine="text-davinci-004",
      prompt=f"Analyze the following contract opportunity and provide an insight on the probability of winning: {description}",
      max_tokens=100
    )
    return response.choices[0].text.strip()

def analyze_opportunities_gpt4(data):
    data['GPT Analysis'] = data['Opportunity Description'].apply(gpt4_analyze_opportunity)
    return data

# Example usage
# analyzed_contracts_gpt4 = analyze_opportunities_gpt4(contracts)

