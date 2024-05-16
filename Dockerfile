FROM python:3.11.6-bookworm
# FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY src .

COPY embeddings embeddings

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]