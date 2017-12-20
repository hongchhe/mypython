FROM ubuntu:16.04
MAINTAINER Hongchuang <hehongchuang@hotmail.com>

COPY    apt/sources.list /etc/apt/
COPY    bin/* /bin/

# install openssh-server, openjdk and wget
RUN     apt-get update \
     && apt-get install -y openssh-server openjdk-8-jdk python3-pip python3 python3-tk wget curl ssh rsync git vim \
     && ln -s /usr/bin/pip3 /usr/bin/pip \
     && ln -s /usr/bin/python3 /usr/bin/python \
     && pip install --upgrade pip \
     && pip install jupyter matplotlib numpy scipy

# set environment variable
ENV     JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 
