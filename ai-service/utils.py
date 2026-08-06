import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq

load_dotenv()

def get_API_key():
    return os.getenv("GROQ_API_KEY")

def respond(message: str):
    groq_api_key = get_API_key()

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=groq_api_key,
        temperature=0.7
    )

    messages = [HumanMessage(content=message)]

    return llm.invoke(messages).content
