FROM python:3.11.0a3-bullseye

# Activate the Virutal Env
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN /bin/bash -c "source /opt/venv/bin/activate"

# System upgrade & Apps instalation
RUN apt update
RUN apt -y upgrade
RUN apt -y install libpq-dev

COPY requirements.txt .
RUN /opt/venv/bin/python3 -m pip install --upgrade pip
RUN /opt/venv/bin/python3 -m pip install --upgrade install -r requirements.txt

WORKDIR /app

ADD . .

# Run local 

# Run at Heroku
