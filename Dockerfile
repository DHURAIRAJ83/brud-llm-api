# Dockerfile - Railway will build this
# We use Ollama official image to simplify hosting small models without heavy Docker steps.
FROM ollama/ollama:latest

# Pull a small CPU-friendly model (change model id later if you prefer)
# Note: 'phi3:mini' used as example. Ollama image must recognize this tag.
RUN ollama pull phi3:mini

# Create app dir and copy API server
WORKDIR /app
# Copy only the FastAPI server and requirements
COPY server.py requirements.txt /app/

# Install Python deps for FastAPI
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install --no-cache-dir -r /app/requirements.txt

# Expose FastAPI port and Ollama port (if needed)
EXPOSE 8000
EXPOSE 11434

# Start both Ollama server and FastAPI.
# Ollama serve runs on port 11434 by default in the container; uvicorn runs FastAPI on 8000.
CMD ["sh", "-c", "ollama serve & uvicorn server:app --host 0.0.0.0 --port 8000"]