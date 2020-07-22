FROM python:3.6

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt \
 && rm /requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./src /project
WORKDIR /project

ENTRYPOINT ["/entrypoint.sh"]
