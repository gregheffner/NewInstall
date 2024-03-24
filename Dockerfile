# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

# copy requirements.txt
COPY requirements.txt .

# Install requirements
RUN pip install -r requirements.txt

# Set working directory
WORKDIR /app

# copy project
COPY src/ .
COPY .env .

ENTRYPOINT ["python", "main.py"]
