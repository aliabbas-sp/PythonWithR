# Pythonwithr

Simple example of how to integrate Python With R using Django and Docker.

## Description

Integration between Python and R using Django and Docker.

## Getting Started

### Dependencies

Tested in Linux and Windows with Python v3.10.4, R v4.1.2 and Django v4.0.1.
See below the list of dependencies

* Python
    * Initial Release
    * Django==4.0.1
    * rpy2==3.4.5
    * psycopg2==2.9.3
    * django-environ==0.8.1
    * gunicorn==20.1.0
    * whitenoise==5.3.0
    * django-heroku==0.3.1
    * asgiref==3.4.1
    * numpy==1.22.0
    * pandas==1.3.5
    * pytz==2021.3
    * python-dateutil==2.8.2
    * six==1.16.0

* R
    * rvest
    * stringr
    * tidyr
    * dplyr
    * languageserver
    * jsonlite
    * rlang

### Deploying program

```
$ heroku container:login
$ heroku container:push web --app <APP-NAME>
$ heroku container:release web
```
## Authors

Abbas, Ali

## Version History

* 0.1
    * Initial Release
