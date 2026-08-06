from fastapi import FastAPI
from pydantic import BaseModel
from utils import respond

app = FastAPI()

class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
def chat_handler(req: ChatRequest):
    response = respond(req.question) 

    return {
            "answer": f"{response}",
            "sources": [
                "demo-source",
                "go.dev"
                ]
            }
