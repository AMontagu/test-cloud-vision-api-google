FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/code

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml .
COPY poetry.lock .
COPY Dresskare-ee12869e8def.json .

ENV GOOGLE_APPLICATION_CREDENTIALS="/opt/code/Dresskare-ee12869e8def.json"

RUN poetry install