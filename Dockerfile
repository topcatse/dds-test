FROM ubuntu:16.04

MAINTAINER Tommy Carlsson

USER root

RUN apt-get update
RUN apt-get -y install wget 
RUN apt-get -y install iptables
RUN apt-get -y install tcpdump

#RUN useradd -m -s /bin/bash dds

#USER dds
RUN mkdir /dds
WORKDIR /dds

ADD /etc/license.lic license.lic
ADD /etc/config config
ADD /lib lib

ENV OSPL_URI=file:///dds/config/ospl.xml
ENV ADLINK_LICENSE=/dds
ENV LD_LIBRARY_PATH=/dds/lib:.

RUN mkdir HelloWorld
WORKDIR /dds/HelloWorld

ADD /examples/dcps/HelloWorld/isocpp2/helloworld helloworld
ADD /examples/dcps/HelloWorld/isocpp2/publisher publisher
ADD /examples/dcps/HelloWorld/isocpp2/subscriber subscriber
ADD /examples/dcps/HelloWorld/isocpp2/*.so ./
ADD /etc/ospl_metaconfig.xml ospl_metaconfig.xml

#USER root
RUN echo root:root | chpasswd

EXPOSE 7400

#CMD ["source /dds/helloworld"]

#docker build --rm --no-cache --tag dds-image .
#docker run --name dds-container --rm -d dds-image
#docker exec -d dds-container -v var:/dds/var -w HelloWorld -e OSPL_URI=file:///dds/var/tcp.xml publisher
#docker run --name=dds-container --hostname=dds --network="bridge" --rm -ti -v `pwd`/var:/dds/var -w /dds/HelloWorld -e OSPL_URI=file:///dds/var/udp.xml dds-image bash
#docker run --name=dds-container --hostname=dds --rm -ti -v `pwd`/var:/dds/var -w /dds/HelloWorld -e OSPL_URI=file:///dds/config/ospl.xml --network="host" --cap-add=NET_ADMIN -p 7400:7400 dds-image bash
#cat /sys/class/net/enp0s3/statistics/rx_bytes
#tcpdump -p udp -w ../var/helloworld.pcap
