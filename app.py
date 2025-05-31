import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Pro model (text-only)
model = genai.GenerativeModel("gemini-2.0-flash-lite")

# Set page title
st.set_page_config(page_title="Gemini Friendly Chatbot")
st.title("🤖 Gemini Friendly Chatbot")

# Initialize chat session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Chat input
user_input = st.text_input("You:", key="user_input")

if user_input:
    # Get response
    response = st.session_state.chat_session.send_message(user_input)

    # Display user and Gemini message
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response.text)
