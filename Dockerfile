FROM python:3.11.0a3-bullseye

#RUN apt -y install r-base
#RUN apt -y install wget

# RUN set -ex \
#     && pip install --upgrade pip \  
#     && pip install --no-cache-dir -r requirements.txt 

# Activate the Virutal Env
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN /bin/bash -c "source /opt/venv/bin/activate"

# System upgrade & Apps instalation
RUN apt update
RUN apt -y upgrade
RUN apt -y install libpq-dev
# RUN wget http://ftp.de.debian.org/debian/pool/main/g/gunicorn/gunicorn_20.1.0-1_all.deb
# RUN apt install -f -y ./gunicorn_20.1.0-1_all.deb

COPY requirements.txt .
RUN /opt/venv/bin/python3 -m pip install --upgrade pip
RUN /opt/venv/bin/python3 -m pip install --upgrade install -r requirements.txt

WORKDIR /app

ADD . .

# Run local 
# EXPOSE 8000
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "pythonwithr.wsgi:application"]

# Run at Heroku
CMD gunicorn pythonwithr.wsgi:application N --bind 0.0.0.0:$PORT
