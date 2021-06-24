FROM python:3.8-buster

LABEL MAINTAINER="HENRIQUE SANTOS"
LABEL VERSION="1.0"

WORKDIR /app

ADD requirements.txt .

RUN python3 -m pip install --upgrade pip && python3 -m pip install --no-cache-dir -r requirements.txt

ENV API_KEY 0c514e9b62bc23e0498ca8eb5a424bb1

COPY . . 

EXPOSE 8000

RUN python3 manage.py migrate

CMD ["sh", "-c", "python3 manage.py runserver 0.0.0.0:8000"]
