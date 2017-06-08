From hongchhe/python:3.6.1
MAINTAINER Hongchuang <hehongchuang@hotmail.com>

RUN        pip install django \
        && groupadd -r django \
        && useradd -r -g django django

# note 8088 is for jupyter notebook
EXPOSE     8000 8088

ENV        USER_HOME=/home/django

RUN        mkdir -p ${USER_HOME} \
        && chown -R django ${USER_HOME} && chgrp -R django ${USER_HOME}

COPY       scripts/* ${USER_HOME}/scripts

WORKDIR    ${USER_HOME}

USER       django

ENTRYPOINT ["${USER_HOME}/scripts/entrypoint.sh"]
