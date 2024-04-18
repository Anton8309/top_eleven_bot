FROM python:3.11
MAINTAINER Anton Demidov 'mario_83.83@mail.ru'
WORKDIR /Bot
COPY bot/bot.py .
COPY bot/.env .
COPY requirements/requirements.txt .
COPY . .

RUN pip install -r requirements.txt

CMD ["python3","bot.py"]


