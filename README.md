# AMC Math Quiz App

Welcome to the AMC Math Quiz App! This app is designed to provide users with an easy and interactive way to practice AMC (American Mathematics Competitions) math questions. The app presents questions from a preloaded set and provides instant feedback on your answers.

## Features

- **Random Questions:** Get a new question each time you start the app or move to the next question.
- **Instant Feedback:** Receive immediate feedback on whether your answer is correct or incorrect.
- **Score Tracking:** Keep track of your score as you progress through the questions.
- **Explanations:** View explanations for the wrong answers.
- **Chatbot Assistance:** Ask the chatbot for help or explanations about the current quiz question.

## File Structure

   ```bash
AMC-QUIZ-APP/
│
├── .env
├── .gitignore
├── amc_quiz.py
├── LICENSE
├── openai_utils.py
├── questions.json
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.7 or higher
- Streamlit
- OpenAI API key
- A JSON file (`questions.json`) containing the quiz questions

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/amc-math-quiz-app.git
   cd amc-math-quiz-app
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the OpenAI API key:**

Create a .env file in the root directory of your project and add your OpenAI API key:

   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **Prepare the questions JSON file:**

Ensure you have a questions.json file in the root directory of your project. This file should contain the quiz questions in the following format:

   ```bash
   [
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "correct_option": "4"
    }
    ...
   ]
   ```

## Running the App

To start the app, navigate to the project directory and run the following command:

   ```bash
   streamlit run streamlit_app.py
   ```

This will start the Streamlit server, and you can access the app by opening a web browser and navigating to http://localhost:8501.

## Usage

### Start the Quiz:
- The app will display a random math question.
- Choose your answer from the provided options and click the "Submit" button.

### View Feedback:
- After submitting your answer, you will receive immediate result on whether if it's correct or incorrect.
- If your answer is incorrect, you can view an explanation by the chatbot.

### Navigate Through Questions:
- Use the "Next Question" button to proceed to the next question.
- Your score will be updated accordingly.

### Reset the Quiz:
- Click the "Clear Questions" button to reset the quiz and start over.

### Chatbot Assistance:
- Ask the chatbot questions about the current quiz question for additional help or explanations.

## Customization
- You can customize the questions by editing the `questions.json` file. Add more questions in the same format to expand the quiz.

## License
- This project is licensed under the MIT License. See the `LICENSE` file for more details.
