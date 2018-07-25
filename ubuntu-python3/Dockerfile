FROM ubuntu:18.04
MAINTAINER Hongchuang <hehongchuang@hotmail.com>

RUN        sed -i /etc/apt/sources.list -e 's/archive.ubuntu.com/cn.archive.ubuntu.com/g' \
        && apt-get update \
        && apt-get -y upgrade \
        && apt-get install -y python3 python3-pip python3-distutils curl vim language-pack-zh-hans \
        && locale-gen en_US.UTF-8
RUN        ln -s /usr/bin/python3 /usr/bin/python \
        && ln -s /usr/bin/pip3 /usr/bin/pip \
        && pip install jupyter \
        && mkdir -p /root/.jupyter
ENV        LANG en_US.UTF-8
ENV        LANGUAGE en_US:en
ENV        LC_ALL en_US.UTF-8
COPY       conf/ /root/.jupyter

EXPOSE     8888

WORKDIR    /root

ENTRYPOINT ["jupyter", "notebook"]
