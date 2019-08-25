FROM python:3.7-slim

RUN apt-get update && apt-get -y install python3-dev build-essential \
libpcre3 libpcre3-dev gettext-base && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . /src
WORKDIR /src

RUN pip install -r requirements.txt

ENTRYPOINT ["./run.sh"]
