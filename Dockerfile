FROM python:3-slim
LABEL maintainer="heewei84@gmail.com"

ENV PROJECT_ROOT /app
WORKDIR $PROJECT_ROOT

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD python3 manage.py runserver 0.0.0.0:8000
