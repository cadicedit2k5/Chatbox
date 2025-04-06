import streamlit as st
from openai import OpenAI

# Track chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]

api_key = st.secrets["api_key"]