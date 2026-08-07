import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq

load_dotenv()

def get_API_key():
    return os.getenv("GROQ_API_KEY")

def respond(message: str, context: str):
    groq_api_key = get_API_key()

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=groq_api_key,
        temperature=0.7
    )

    input = f"answer this question {message} using this contxt {context} IF NEEDED, if its a question not related to this source reply normally"
    messages = [HumanMessage(content=input)]

    return llm.invoke(messages).content
