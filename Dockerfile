FROM python:3.10.1-bullseye
#FROM python:3.11.0a3-bullseye

# Activate the Virutal Env
#ENV VIRTUAL_ENV=/opt/venv
#RUN python3 -m venv $VIRTUAL_ENV
#ENV PATH="$VIRTUAL_ENV/bin:$PATH"
#RUN /bin/bash -c "source /opt/venv/bin/activate"

# System upgrade & Apps instalation

RUN apt update
RUN apt -y upgrade
RUN apt -y install libpq-dev r-base wget
RUN wget https://download1.rstudio.org/desktop/bionic/amd64/rstudio-2021.09.0-351-amd64.deb
RUN apt install -f -y ./rstudio-2021.09.0-351-amd64.deb
#RUN apt -y install gcc python3-dev python3-pip python3-venv python3-wheel

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --upgrade install -r requirements.txt

WORKDIR /app

ADD . .

# Run local 
#EXPOSE 8000
#CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "pythonwithr.wsgi:application", "--timeout", "120"]

# Run at Heroku
CMD gunicorn pythonwithr.wsgi:application N --bind 0.0.0.0:$PORT
