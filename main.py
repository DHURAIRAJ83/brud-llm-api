# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Brud LLM API")

# Data model for chat input
class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "Brud LLM API is running successfully!"}

@app.post("/chat")
def chat(request: ChatRequest):
    user_input = request.prompt
    # Simple dummy model logic (you can replace with LLM later)
    if "code" in user_input.lower():
        response = "Sure! I can help you with Python coding examples."
    else:
        response = f"You said: {user_input}"
    return {"reply": response}