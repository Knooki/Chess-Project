FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1 \ PYTHONUNBUFFERED=1 

WORKDIR /root/home/knooki/dev/chess_project/backend/

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir -r ~/home/knooki/dev/chess_project/backend/requirements.txt

COPY . .