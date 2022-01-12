FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt update
RUN apt -y upgrade

RUN apt -y install r-base

RUN apt -y install wget
RUN wget https://download1.rstudio.org/desktop/bionic/amd64/rstudio-2021.09.0-351-amd64.deb
RUN apt install -f -y ./rstudio-2021.09.0-351-amd64.deb

RUN apt -f install

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
