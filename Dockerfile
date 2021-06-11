FROM python:3.9.5-alpine3.13

RUN apk update && apk upgrade && apk add bash; mkdir /project;
#apk add npm;
WORKDIR /project

#COPY ./requirements.txt .
#RUN pip install -r requirements.txt

EXPOSE 3000
#
#FROM python:3.8-slim-buster
#
#ENV VIRTUAL_ENV=/opt/venv
#RUN python3 -m venv $VIRTUAL_ENV
#ENV PATH="$VIRTUAL_ENV/bin:$PATH"
#
## Install dependencies:
#COPY requirements.txt .
#RUN pip install -r requirements.txt
#
## Run the application:
#COPY myapp.py .
#CMD ["python", "myapp.py"]