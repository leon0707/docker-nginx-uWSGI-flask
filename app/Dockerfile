FROM python:3.7-slim

RUN apt-get update && apt-get -y install python3-dev build-essential \
libpcre3 libpcre3-dev

COPY . /src
WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 3000

ENTRYPOINT ["./run.sh"]
