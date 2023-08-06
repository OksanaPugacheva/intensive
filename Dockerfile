FROM python:3.10-slim

RUN pip install poetry
COPY cafe_api /app/cafe_api

COPY poetry.lock pyproject.toml README.md /app/

WORKDIR /app

RUN poetry install
