FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code
WORKDIR /code
COPY app/. /code
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD . /code
