FROM python:3.8

ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip3 install django
RUN pip3 install psycopg2-binary
RUN pip3 install djangorestframework
RUN pip3 install jsonfield
RUN pip3 install requests