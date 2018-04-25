FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements/base.txt /code/
ADD requirements/development.txt /code/
RUN pip install -r base.txt
RUN pip install -r development.txt
ADD . /code/
# ad gettext for makemessages command
RUN apt-get update && apt-get install -y gettext