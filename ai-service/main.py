from fastapi import FastAPI
from pydantic import BaseModel
from utils import respond
from scraper.scraper import scrape

app = FastAPI()

class ChatRequest(BaseModel):
    question: str
    url: str

@app.post("/chat")
def chat_handler(req: ChatRequest):
    context = scrape(req.url)
    response = respond(req.question, context)

    return {
        "answer": response,
        "sources": [
            f"{req.url}"
        ]
    }