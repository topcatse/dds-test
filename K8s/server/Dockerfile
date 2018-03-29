FROM python:3

MAINTAINER Tommy Carlsson

USER root

RUN mkdir /dds
WORKDIR /dds

#RUN pip install --no-cache-dir 

COPY *.py ./

CMD [ "python", "server.py" ]