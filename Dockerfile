FROM python:3.12

WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
