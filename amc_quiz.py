import streamlit as st
import random
import json
from openai_utils import get_explanation, ask_question

# Load questions from the JSON file
with open('questions.json', 'r') as file:
    questions = json.load(file)

# Function to get a random question
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
        .title {
            text-align: center;
            font-size: 2.5em;
            color: #4CAF50;
        }
        .question {
            font-size: 1.2em;
            margin-top: 20px;
            margin-bottom: 10px;
            color: #333;
        }
        .radio-label {
            font-size: 1em;
            color: #555;
        }
        .btn-container {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }
        .score {
            font-size: 1.5em;
            color: #4CAF50;
            margin-top: 30px;
        }
        .explanation {
            margin-top: 10px;
            color: #000;
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown("<div class='title'>AMC Quiz App</div>", unsafe_allow_html=True)

# Display the current question
current_question_idx = st.session_state.current_question_idx
if current_question_idx < len(st.session_state.questions):
    question = st.session_state.questions[current_question_idx]
    st.markdown(f"<div class='question'><strong>Question {current_question_idx + 1}:</strong> {question['question']}</div>", unsafe_allow_html=True)
    options = question['options']

    # Create a radio button for options
    user_answer = st.radio("Choose an answer:", options, key=f"q{current_question_idx}")

    if st.button("Submit"):
        st.session_state.user_answers[current_question_idx] = user_answer
        if user_answer == question['correct_option']:
            st.session_state.score += 1
            st.success("Correct!")
        else:
            st.error("Incorrect.")
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

    # Navigation buttons
    st.markdown("<div class='btn-container'>", unsafe_allow_html=True)
    if st.button("Next Question"):
        if current_question_idx + 1 < len(st.session_state.questions):
            st.session_state.current_question_idx += 1
        else:
            add_question()
        st.experimental_rerun()
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='score'>No more questions available.</div>", unsafe_allow_html=True)

# Clear questions button
if st.button("Clear Questions"):
    reset_app()
    st.experimental_rerun()

# Display the score
st.markdown(f"<div class='score'>Score: {st.session_state.score}/{st.session_state.current_question_idx + 1}</div>", unsafe_allow_html=True)

# Chatbot feature
st.markdown("### Chatbot")
user_question = st.text_input("Ask a question about the current quiz question:")
if st.button("Ask Chatbot"):
    current_question = st.session_state.questions[current_question_idx]['question']
    chatbot_response = ask_question(current_question, user_question)
    st.markdown(f"**Chatbot:** {chatbot_response}")
