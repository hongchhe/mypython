From hongchhe/ubuntu-python:latest
MAINTAINER Hongchuang <hehongchuang@hotmail.com>

# install openssh-server, openjdk and wget
RUN        pip install django \ 
        && cd /opt \
        && django-admin startproject mysite

EXPOSE     8000

ENTRYPOINT ["/opt/mysite/manage.py", "runserver", "localhost:8000"]
