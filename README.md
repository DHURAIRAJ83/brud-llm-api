# brud-llm-api

Minimal FastAPI wrapper that proxies requests to a model server inside the container.

## Deploy flow
1. Push this repo to GitHub.
2. Connect the repo to Railway (Deploy from GitHub).
3. Set Railway Environment Variables:
   - API_KEY : (your secret)
   - MODEL_NAME : optional model tag (default phi3:mini)
   - INTERNAL_MODEL_API : optional override for model server URL

## Endpoints
POST /generate
Headers: x-api-key: <API_KEY>
Body: { "prompt": "text", "max_tokens": 150 }
