import streamlit as st
import random
import json
from openai_utils import get_explanation, ask_question

# Load questions from the JSON file
with open('questions.json', 'r') as file:
    questions = json.load(file)

def get_random_question():
    return random.choice(questions)

# Initialize session state
if 'questions' not in st.session_state:
    st.session_state.questions = [get_random_question()]
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_question_idx' not in st.session_state:
    st.session_state.current_question_idx = 0
if 'show_explanation' not in st.session_state:
    st.session_state.show_explanation = [False]
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = [None]

def reset_app():
    st.session_state.questions = [get_random_question()]
    st.session_state.score = 0
    st.session_state.current_question_idx = 0
    st.session_state.show_explanation = [False]
    st.session_state.user_answers = [None]

def add_question():
    st.session_state.questions.append(get_random_question())
    st.session_state.show_explanation.append(False)
    st.session_state.user_answers.append(None)

# Custom CSS for styling
st.markdown("""
    <style>
        body { background-color: #f0f2f6; color: #333; font-family: Arial, sans-serif; }
        .title { text-align: center; font-size: 3em; color: #ffffff; background-color: #4caf50; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
        .question { font-size: 1.5em; margin: 20px 0; color: #333; background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
        .radio-label { font-size: 1.2em; }
        .btn-container { display: flex; justify-content: space-between; margin: 20px 0; }
        .score { font-size: 2em; color: #333; margin: 20px 0 10px 0; background-color: #ffffff; padding: 10px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
        .explanation { margin-top: 10px; color: #333; background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
        .chatbot { margin-top: 10px; padding: 20px; background-color: #ffffff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
        .container { display: flex; justify-content: center; align-items: center; flex-direction: column; padding: 20px; }
        .button { background-color: #007BFF; color: white; font-size: 1.2em; padding: 10px; border: none; border-radius: 5px; cursor: pointer; width: 100%; margin-top: 10px; }
        .button:hover { background-color: #0056b3; }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown("<div class='title'>AMC Quiz App</div>", unsafe_allow_html=True)

# Main container
st.markdown("<div class='container'>", unsafe_allow_html=True)

current_question_idx = st.session_state.current_question_idx
if current_question_idx < len(st.session_state.questions):
    question = st.session_state.questions[current_question_idx]
    st.markdown(f"<div class='question'><strong>Question {current_question_idx + 1}:</strong> {question['question']}</div>", unsafe_allow_html=True)
    options = question['options']

    user_answer = st.radio("Choose an answer:", options, key=f"q{current_question_idx}", label_visibility="collapsed")

    if st.button("Submit", key="submit", use_container_width=True):
        st.session_state.user_answers[current_question_idx] = user_answer
        if user_answer == question['correct_option']:
            st.session_state.score += 1
            st.success("Correct!", icon="✅")
        else:
            st.error("Incorrect.", icon="❌")
            st.session_state.show_explanation[current_question_idx] = True
        st.experimental_rerun()

    if st.session_state.user_answers[current_question_idx] is not None:
        st.markdown(f"**Your answer:** {st.session_state.user_answers[current_question_idx]}")
        if st.session_state.user_answers[current_question_idx] == question['correct_option']:
            st.success("Correct!")
        else:
            st.error("Incorrect.")
            if st.session_state.show_explanation[current_question_idx]:
                explanation = get_explanation(question['question'], question['correct_option'])
                st.markdown(f"<div class='explanation'><strong>Explanation:</strong> {explanation}</div>", unsafe_allow_html=True)

    st.markdown("<div class='btn-container'>", unsafe_allow_html=True)
    if st.button("Next Question", key="next", use_container_width=True):
        if current_question_idx + 1 < len(st.session_state.questions):
            st.session_state.current_question_idx += 1
        else:
            add_question()
        st.experimental_rerun()
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='score'>No more questions available.</div>", unsafe_allow_html=True)

if st.button("Clear Questions", key="clear", use_container_width=True):
    reset_app()
    st.experimental_rerun()

st.markdown(f"<div class='score'>Score: {st.session_state.score}/{st.session_state.current_question_idx + 1}</div>", unsafe_allow_html=True)

st.markdown("<div class='chatbot'>", unsafe_allow_html=True)
st.markdown("### Chatbot")
user_question = st.text_input("Ask a question about the current quiz question:")
if st.button("Ask Chatbot", key="ask", use_container_width=True):
    current_question = st.session_state.questions[current_question_idx]['question']
    chatbot_response = ask_question(current_question, user_question)
    st.markdown(f"**Chatbot:** {chatbot_response}")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # Close main container
