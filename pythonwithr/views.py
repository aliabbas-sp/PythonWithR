from django.shortcuts import render
from runr.main import *
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def index(request):
    return render(request, 'home.html')


def exec_rscript(request):
    rscript_result = runr()
    rscript = open(BASE_DIR / 'runr/getsuperbowlresults.r', "r").read()
    return render(request, 'runr.html', {'rscript_result': rscript_result, 'rscript': rscript})


def get_example(request):
    rscript = open(BASE_DIR / 'runr/getsuperbowlresults.r', "r").read()
    return render(request, 'runr.html', {'rscript': rscript})
