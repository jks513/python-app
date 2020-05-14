# TODO:  set base image as ubuntu version 18.04


# TODO:  set maintainer as your pair names


RUN apt-get update -y && \
    apt-get install -y \
    python3 \
    python3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

# TODO: set the command parameter to the app.py file

