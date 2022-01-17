FROM aliabbassp/python_r:3.10_6.3
# based in FROM python:3.10.1-bullseye

# Activate the Virutal Env
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN /bin/bash -c "source /opt/venv/bin/activate"

COPY requirements.txt .
#
RUN pip install --upgrade pip
#
RUN pip install --upgrade install -r requirements.txt
#
WORKDIR /app
#
ADD . .

# Run local 
# EXPOSE 8000
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "pythonwithr.wsgi:application", "--timeout", "120"]

# Run at Heroku
CMD gunicorn pythonwithr.wsgi:application N --bind 0.0.0.0:$PORT
