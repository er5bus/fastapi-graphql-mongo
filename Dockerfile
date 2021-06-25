FROM python:3.6

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY ./src /app/src
WORKDIR /app/src

EXPOSE 5000
# This will not be overriden when docker-compose call command label
CMD uvicorn main:app --port 5000 --host 0.0.0.0 --reload
