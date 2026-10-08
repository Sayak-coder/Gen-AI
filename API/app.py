from fastapi import FastAPI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import os
import uvicorn

from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
if not google_api_key:
    raise RuntimeError("Set GOOGLE_API_KEY or GEMINI_API_KEY before starting the API.")
os.environ["GOOGLE_API_KEY"] = google_api_key

app= FastAPI(
    title="Langchain Google Generative AI Chatbot",
    version="0.1.0",
    description="A simple api serve"
)

model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

add_routes(
    app,
    model,
    path="/google-genai_chatbot"
)

# prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please response to the user queries"),
    ("user","Question: {question}")
])

add_routes(
    app,
    prompt | model,
    path="/chatbot"
)

if __name__=='__main__':
    uvicorn.run(app,host='localhost',port=8000)