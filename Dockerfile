FROM python:3.9.5-alpine

LABEL MAINTAINER="HENRIQUE SANTOS"
LABEL VERSION="1.0"

RUN addgroup -S apigroup && adduser -S weatherapi -G apigroup

WORKDIR /app

ADD requirements.txt .

RUN apk update && apk upgrade

RUN python3 -m pip install --upgrade pip && python3 -m pip install --no-cache-dir -r requirements.txt

ENV API_KEY 0c514e9b62bc23e0498ca8eb5a424bb1

COPY . . 

USER root
EXPOSE 8000
RUN chmod 777 db.sqlite3

USER weatherapi

RUN python3 manage.py migrate

CMD ["sh", "-c", "python3 manage.py runserver 0.0.0.0:8000"]
