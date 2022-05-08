FROM python:3.9-slim-buster

RUN apt-get update && apt-get -yy install gcc libmariadb-dev

WORKDIR /vagrant/build-dockerfile

#COPY /vagrant/api/requirements.txt /vagrant/api/*.py /vagrant/build-dockerfile

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3","./api.py"]