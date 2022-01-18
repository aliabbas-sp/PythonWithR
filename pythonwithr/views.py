from runr.main import *
from pathlib import Path
from django.shortcuts import render
from pythonwithr.forms import RscriptForm
from runr.models import Rscript

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def index(request):
    form = RscriptForm
    return render(request, 'home.html', {'form': form})


def exec_rscript(response):
    form = RscriptForm(response.POST)
    if response.method == 'POST':
        if form.is_valid():
            rscript = form.data["Rscript_code"]
            rscript_result = runr(rscript)
            return render(response, 'runr.html', {'rscript_result': rscript_result, 'form': form})
    return render(response, 'home.html', {'form': form})


def get_sample(request):
    rscript = open(BASE_DIR / 'runr/rscript_sample.r', "r").read()
    form = RscriptForm(request.POST)

    # remember old state
    _mutable = form.data._mutable
    # set to mutable
    form.data._mutable = True
    # сhange the values you want
    form.data["Rscript_code"] = rscript
    # set mutable flag back
    form.data._mutable = _mutable

    context = {
        'form': form
    }
    return render(request, 'home.html', context=context)
