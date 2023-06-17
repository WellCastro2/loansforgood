FROM python:3.8.5

EXPOSE 9000

ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

COPY . /code/