import openai
import json
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_explanation(question, correct_option):
    prompt = f"Explain why the correct answer to the question '{question}' is '{correct_option}'."
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    explanation = response.choices[0].text.strip()
    return explanation

def ask_question(current_question, user_question):
    prompt = f"Given the current question: '{current_question}', answer the following question: {user_question}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choices[0].text.strip()
    return answer
