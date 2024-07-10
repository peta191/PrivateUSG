import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Or replace with your API key string

def gpt_generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def generate_proposal_outline(contract_description, capabilities):
    prompt = f"Based on the following contract description, generate a proposal outline highlighting the strengths of ZOECONN Consulting:\n\nContract Description: {contract_description}\n\nCapabilities: {capabilities}"
    return gpt_generate_response(prompt)

def generate_summary(contract_details):
    prompt = f"Summarize the following contract details:\n\n{contract_details}"
    return gpt_generate_response(prompt)

def generate_email_intro(contract_details):
    prompt = f"Write an introductory email draft for the following contract opportunity:\n\n{contract_details}"
    return gpt_generate_response(prompt)

