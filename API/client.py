import requests
import streamlit as st

def get_gemi_response(input_text):
    response = requests.post("http://localhost:8000/chatbot/invoke",
    json={"input": {"question": input_text}})
    response.raise_for_status()
    return response.json()['output']['content']

st.title("Langchain Google Genertive AI Chatbot")
input_text=st.text_input("Enter how can I help you: ")

if input_text:
    st.write(get_gemi_response(input_text))