FROM python:3.11

RUN pip install poetry
RUN mkdir -p /app
COPY . /app

WORKDIR /app

RUN poetry install

CMD [ "poetry", "run", "start"]