from django.shortcuts import render
from runr.main import *
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def index(request):
    return render(request, 'home.html')


def exec_rscript(request):
    superbowlresults = runr()
    tab_class = "table"
    superbowlresults = superbowlresults.replace("<thead>", "<table class=""" + tab_class + ">""")
    rscript = open(BASE_DIR / 'runr/getsuperbowlresults.txt', "r").read()
    return render(request, 'runr.html', {'superbowlresults': superbowlresults, 'rscript': rscript})


def get_example(request):
    rscript = open(BASE_DIR / 'runr/getsuperbowlresults.txt', "r").read()
    return render(request, 'runr.html', {'rscript': rscript})
