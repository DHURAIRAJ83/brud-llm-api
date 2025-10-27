from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Small open-source model
generator = pipeline("text-generation", model="distilgpt2")

@app.get("/")
def home():
    return {"message": "Welcome to Brud LLM API!"}

@app.post("/generate/")
def generate_text(prompt: str):
    result = generator(prompt, max_length=100, num_return_sequences=1)
    return {"prompt": prompt, "response": result[0]['generated_text']}