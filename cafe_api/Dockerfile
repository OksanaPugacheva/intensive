FROM python:3.10-slim

RUN pip install poetry
COPY . /app/cafe_api

COPY README.md poetry.lock pyproject.toml /app/

WORKDIR /app

RUN poetry install