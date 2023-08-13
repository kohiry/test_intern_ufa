FROM python:alpine

WORKDIR /app
COPY pyproject.toml /app/
COPY poetry.lock /app/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install
COPY . /app/
