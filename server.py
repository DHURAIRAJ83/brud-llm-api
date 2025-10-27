# server.py
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import os
import requests

app = FastAPI()

# API_KEY will be injected from Railway environment variables
API_KEY = os.getenv("API_KEY", "mysecretkey")

# Replace the INTERNAL_MODEL_API with the model server endpoint used in the container.
# For the initial setup we will assume the model server runs inside the same container
# and exposes a local HTTP endpoint (example used later in Dockerfile).
INTERNAL_MODEL_API = os.getenv("INTERNAL_MODEL_API", "http://localhost:11434/api/generate")

class GenReq(BaseModel):
    prompt: str
    max_tokens: int = 150

@app.post("/generate")
async def generate(req: GenReq, x_api_key: str = Header(None)):
    # Simple API key check
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    payload = {
        "model": os.getenv("MODEL_NAME", "phi3:mini"),
        "prompt": req.prompt,
        "max_tokens": req.max_tokens
    }
    try:
        resp = requests.post(INTERNAL_MODEL_API, json=payload, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        # adapt to the model-server response shape; here we try common keys
        if isinstance(data, dict) and ("response" in data or "result" in data):
            return {"response": data.get("response") or data.get("result")}
        return {"response": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model server error: {e}")
