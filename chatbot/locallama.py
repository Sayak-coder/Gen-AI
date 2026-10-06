from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
if not google_api_key:
    st.error(
        "GOOGLE_API_KEY or GEMINI_API_KEY is not set. "
        "Add one to .env or your environment."
    )
    st.stop()

os.environ["GOOGLE_API_KEY"] = google_api_key
os.environ['LANGCHAIN_TRACING_V2']='true'
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
if langchain_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

#prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please response to the user queries"),
    ("user","Question: {question}")
])

#streamlit framework
st.title("Langchain Ollama Chatbot")
input_text=st.text_input("Enter your question here: ")

llm = Ollama(model="gemma4")
output_parser=StrOutputParser()
chain= prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))