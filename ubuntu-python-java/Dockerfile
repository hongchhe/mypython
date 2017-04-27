From ubuntu:16.04
MAINTAINER Hongchuang <hehongchuang@hotmail.com>

# install openssh-server, openjdk and wget
RUN     apt-get update \
     && apt-get install -y openssh-server openjdk-8-jdk python-pip python3-pip python ipython ipython-notebook wget curl ssh rsync git vim \
     && pip install --upgrade pip

# set environment variable
ENV     JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 
