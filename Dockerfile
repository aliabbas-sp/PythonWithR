FROM python:3

#
WORKDIR /app
#
## By copying over requirements first, we make sure that Docker will cache
## our installed requirements rather than reinstall them on every build
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Now copy in our code, and run it
COPY . /app
#EXPOSE 8000
CMD ["python"],["--bind"],["0.0.0.0:8000"],["{pythonwithr}.wsgi"]

#CMD [ "python", "./your-daemon-or-script.py" ]
#
#
#ENV DEBIAN_FRONTEND=noninteractive
#
##RUN apt-get update
##RUN apt-get install python3 -y
##RUN apt-get install python3-pip -y
##RUN apt-get install vim -y
#
#RUN pip install install Django==4.0.1
#RUN pip install gunicorn==20.1.0
#RUN pip install whitenoise==5.3.0
#RUN pip install django-environ==0.8.1
#RUN pip install asgiref==3.4.1
#RUN pip install dj-database-url==0.5.0
#RUN pip install pytz==2021.3
#RUN pip install django-heroku==0.3.1
#RUN pip install psycopg2==2.9.3
##RUN pip install rpy2==3.4.5
#
#WORKDIR /app
#COPY . /app
#EXPOSE 8000
#
#ENTRYPOINT ["python3"]
#
#RUN python manage.py runserver 0.0.0.0:8000

#FROM python:3.10.1
#
#WORKDIR /app
#
## By copying over requirements first, we make sure that Docker will cache
## our installed requirements rather than reinstall them on every build
#COPY requirements.txt /app/requirements.txt
#RUN pip install -r requirements.txt
#
## Now copy in our code, and run it
#COPY . /app
#EXPOSE 8000
#RUN python manage.py runserver 0.0.0.0:8000
