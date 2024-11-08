import sys
import re
import streamlit as st
from langchain_community.llms import LlamaCpp
from services.logging import Logger
from services.actions import run_service


LOG_SAVE = True
SAVE_TO_SINGLE_FILE = True

# Global Variables
# llama model
llm = LlamaCpp(
            model_path="models/llama-2-7b-chat.Q4_K_S.gguf",
            n_gpu_layers=40,
            n_batch=512,  # Batch size for model processing
            verbose=False,  # Enable detailed logging for debugging
        )



# Create a logger object
# Initialize Logger
logger = Logger("log") if LOG_SAVE else None

def initialize():
    # Streamlit UI setup
    # Configure the page
    st.set_page_config(page_title="Study Chatbot", layout="centered")
    st.title("Study Bot")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def get_user_input():
    st.write("### Ask a question")
    return st.text_input("Type your message here...", key="question")

def generate_response(question):
    with st.spinner("Generating response..."):
        response = run_service(llm, question, logger)
    return response

def update_chat_history(question, response):
    # Insert messages at the beginning of the chat history
    st.session_state.chat_history.insert(0, {"role": "chatbot", "content": response})
    st.session_state.chat_history.insert(0, {"role": "user", "content": question})
    

def display_chat_history():
    st.write("### Chat History")
    for chat in st.session_state.chat_history:
        role = "**You:**" if chat["role"] == "user" else "**Chatbot:**"
        st.write(f"{role} {chat['content']}")


def main():
    initialize()
    question = get_user_input()

    # Check if the "Send" button is pressed and the question is not empty
    if st.button("Send") and question:
        response = generate_response(question)
        update_chat_history(question, response)
        #st.session_state.question = ""  # Clear the input field after submission

    display_chat_history()
    if "chat_history" in st.session_state and st.session_state.chat_history:
        print(st.session_state.chat_history)
        text = ""
        for chat in reversed(st.session_state.chat_history):  # Reverse to save in chronological order
            role = "You: " if chat["role"] == "user" else "Chatbot: "
            text = f'\n{role} {chat['content']}' + text + '\n'
        st.download_button("Save", data=text)

if __name__ == "__main__":
    main()

