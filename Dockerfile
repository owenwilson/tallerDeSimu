FROM ubuntu:20.04
MAINTAINER owenwilson
RUN apt-get update -y && \
    apt-get install -y python3-pip build-essential libssl-dev libffi-dev python3-dev

# We copy just the requirements.txt first to leverage Docker cache
RUN mkdir -p /app
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "index.py" ]
