FROM python:3.9-slim-buster

RUN apt-get update && apt-get -yy install gcc libmariadb-dev

WORKDIR /api

COPY ["requirements.txt", "api.py", "config.py", "./"] 

RUN pip3 install -r requirements.txt



EXPOSE 5000

CMD ["python3","./api.py"]