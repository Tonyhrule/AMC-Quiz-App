from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
import json
from dotenv import load_dotenv
import os

load_dotenv()


def get_explanation(question, correct_option):
    prompt = f"Explain why the correct answer to the question '{question}' is '{correct_option}'."
    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ])
    explanation = response.choices[0].message.content.strip()
    return explanation

def ask_question(current_question, user_question):
    prompt = f"Given the current question: '{current_question}', answer the following question: {user_question}"
    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ])
    answer = response.choices[0].message.content.strip()
    return answer
