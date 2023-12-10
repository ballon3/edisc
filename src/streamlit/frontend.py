import streamlit as st
import requests

# URL of your FastAPI server
API_URL = "http://localhost:8000/api"

# Function to get flashcards from the FastAPI backend
def get_flashcards():
    response = requests.get(f"{API_URL}/flashcards/")
    return response.json()

# Function to send practice response to the FastAPI backend
def send_practice_response(translation):
    response = requests.post(f"{API_URL}/practice/", json={"translation": translation})
    return response.json()

# Function to get progress from the FastAPI backend
def get_progress():
    correct_answers = st.session_state.get('correct_answers', 0)
    response = requests.get(f"{API_URL}/progress/", params={"correct_answers": correct_answers})
    return response.json()

def main():
    st.title("AI-Powered Language Learning App")

    # Navigation
    page = st.sidebar.selectbox("Choose a page", ["Home", "Learn", "Practice", "Progress"])

    if page == "Home":
        home_page()
    elif page == "Learn":
        learn_page()
    elif page == "Practice":
        practice_page()
    elif page == "Progress":
        progress_page()

def home_page():
    st.write("Welcome to the AI-Powered Language Learning App.")

def learn_page():
    st.write("Learn new words and phrases here.")
    flashcards = get_flashcards()
    word_index = st.slider("Choose a word", 0, len(flashcards)-1, 0)
    word = flashcards[word_index]["word"]
    meaning = flashcards[word_index]["meaning"]

    st.write("Word:", word)
    if st.button("Show Meaning"):
        st.write("Meaning:", meaning)

def practice_page():
    st.write("Practice your skills here.")
    user_input = st.text_input("Translate 'Hello' into Chinese")
    if user_input:
        result = send_practice_response(user_input)
        if result["correct"]:
            st.success("Correct!")
            # Update session state for correct answers
            st.session_state['correct_answers'] = st.session_state.get('correct_answers', 0) + 1
        else:
            st.error("Try again!")

def progress_page():
    st.write("Track your progress here.")
    progress = get_progress()
    st.write("Your progress:")
    st.write("Correct Answers:", progress["correct_answers"])

if __name__ == "__main__":
    main()
