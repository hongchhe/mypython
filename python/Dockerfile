# As for the base images, please refer to https://hub.docker.com/_/python/
From python:3.6.1
MAINTAINER Hongchuang <hehongchuang@hotmail.com>

# install openssh-server
RUN        apt-get update \
        && apt-get install -y openssh-server vim \
        && pip install jupyter matplotlib numpy scipy

COPY       bin/* /bin/
