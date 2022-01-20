import runr.main
from runr.main import *
from pathlib import Path
from django.shortcuts import render
from pythonwithr.forms import RscriptForm
from django.http import HttpResponse, Http404
import pandas as pd
import os
from runr.models import Rscript

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def index(request):
    form = RscriptForm
    return render(request, 'home.html', {'form': form})


def get_data_json(request):

    return render(request, 'data.json')


def exec_rscript(response):
    form = RscriptForm(response.POST)
    if form.is_valid():
        if response.method == 'POST':
            rscript = form.data["Rscript_code"]
            if 'execute' in response.POST:
                try:
                    rscript_result = runr(rscript)
                except Exception as e:
                    rscript_result = f"<div class=\"d-flex justify-content-center\">\
                                        <div class=\"alert alert-danger\" role=\"alert\">\
                                        Oops, an error occurred when trying to execute your code</div>"
                return render(response, 'runr.html', {'rscript_result': rscript_result, 'form': form})

            elif 'download' in response.POST:
                try:
                    filename = save_file(rscript)

                    with open(f"runr/export/"+filename, 'rb') as excel:
                        data = excel.read()
                    response = HttpResponse(data,
                                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                    response['Content-Disposition'] = f'attachment; filename='+filename
                    return response

                except Exception as e:
                    rscript_result = f"<div class=\"d-flex justify-content-center\">\
                                            <div class=\"alert alert-danger\" role=\"alert\">\
                                            Oops, an error occurred when trying to execute your code</div>"
                return render(response, 'runr.html', {'rscript_result': rscript_result, 'form': form})


def get_sample(request):
    rscript = open(BASE_DIR / 'runr/rscript_sample.r', "r").read()
    form = RscriptForm(request.POST)

    _mutable = form.data._mutable
    form.data._mutable = True
    form.data["Rscript_code"] = rscript
    form.data._mutable = _mutable

    context = {
        'form': form
    }
    return render(request, 'home.html', context=context)
