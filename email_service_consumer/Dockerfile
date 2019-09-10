FROM python:3.7-slim

RUN apt-get update && apt-get -y install python3-dev build-essential \
&& apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . /src
WORKDIR /src

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "consumer.py"]
