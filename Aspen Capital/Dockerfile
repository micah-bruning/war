# syntax=docker/dockerfile:1

FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python3 -m unittest tests/test_card.py
RUN python3 -m unittest tests/test_game.py

CMD [ "python3", "./app.py"]

