FROM python:3.9.12-slim

WORKDIR /main

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_RUN_HOST=0.0.0.0

COPY . .

EXPOSE 5000




