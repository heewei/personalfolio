FROM python:3-slim
LABEL maintainer="heewei84@gmail.com"

ENV PROJECT_ROOT /app
WORKDIR $PROJECT_ROOT

COPY requirements.txt requirements
RUN pip install -r requirements
COPY . .
CMD python manage.py runserver 0.0.0.0:8001