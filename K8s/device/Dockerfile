FROM python:3

MAINTAINER Tommy Carlsson

USER root

RUN mkdir /dds
WORKDIR /dds

#RUN pip install --no-cache-dir 

COPY device.py ./

CMD [ "python", "device.py" ]