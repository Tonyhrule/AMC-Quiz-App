import openai
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key here
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_explanation(question, correct_option):
    prompt = f"Explain why the correct answer to the question '{question}' is '{correct_option}'."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    explanation = response['choices'][0]['message']['content'].strip()
    return explanation

def ask_question(current_question, user_question):
    prompt = f"Given the current question: '{current_question}', answer the following question: {user_question}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    answer = response['choices'][0]['message']['content'].strip()
    return answer
