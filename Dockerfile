# Build image
# docker build -t removebackgroundapi .
#
# run image
# docker run -p 8000:8000 removebackgroundapi

FROM python:3.11-slim

WORKDIR /app

# Copy the local code to the Docker container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Inform Docker that the container listens on the specified network ports at runtime.
EXPOSE 8000

CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]