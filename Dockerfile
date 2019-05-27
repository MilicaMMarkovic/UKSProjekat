FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY app/. /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8011
CMD python manage.py runserver 0.0.0.0:8011
