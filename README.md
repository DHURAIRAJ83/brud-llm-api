# brud-llm-api

A simple LLM API using Hugging Face Transformers.

## Deploy flow
1. Push this repo to GitHub.
2. Connect the repo to Railway (Deploy from GitHub).
3. Set Railway Environment Variables (none required for basic use).

## Endpoints
GET /
Returns welcome message.

POST /generate/
Body: {"prompt": "your text"}
Returns generated text using distilgpt2 model.
