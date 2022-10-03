from runr.main import *
from pathlib import Path
from django.shortcuts import render
from pythonwithr.forms import RscriptForm
from django.http import HttpResponse

BASE_DIR = Path(__file__).resolve().parent.parent


def index(request):
    form = RscriptForm
    return render(request, 'home.html', {'form': form})


def exec_rscript(request):
    form = RscriptForm(request.POST)
    if form.is_valid():
        if request.method == 'POST':
            script = form.data["script"]
            if 'execute' in request.POST:
                try:
                    result_table, filename = execute(script)

                    mutable_script = form.data._mutable
                    form.data._mutable = True
                    form.data["df"] = filename
                    form.data._mutable = mutable_script

                except Exception as error:
                    mutable_script = form.data._mutable
                    form.data._mutable = True
                    form.data["df"] = None
                    form.data._mutable = mutable_script
                    error_message = f"<div class=\"d-flex justify-content-center\" style=\"margin-left: 15%;"\
                                    f"margin-right:15%; text-align: center\"> <div class=\"alert alert-danger\""\
                                    f"role=\"alert\"> Oops, an error occurred when trying to execute your code.<br><br>\
                                    <b>Details: </b>{error} </div> </div>"
                    return render(request, 'runr.html',
                                  {'error_message': error_message, 'form': form})
                else:
                    return render(request, 'runr.html',
                                  {'result_table': result_table, 'filename': filename, 'form': form})

            elif 'download' in request.POST:
                try:
                    filename = form.data["df"]
                    if filename == "":
                        error_message = f"<div class=\"d-flex justify-content-center\" style=\"margin-left: 15%; " \
                                        f"margin-right:15%; text-align: center\"> <div class=\"alert alert-danger\" " \
                                        f"role=\"alert\"> Run your script before trying to download. </div> </div>"

                        return render(request, 'runr.html', {'error_message': error_message, 'form': form})
                except Exception as error:
                    error_message = f"<div class=\"d-flex justify-content-center\" style=\"margin-left: 15%;"\
                                    f"margin-right:15%; text-align: center\"> <div class=\"alert alert-danger\""\
                                    f"role=\"alert\"> Oops, an error occurred when trying to execute your code.<br><br>\
                                    <b>Details: </b>{error} </div> </div>"

                    return render(request, 'runr.html', {'error_message': error_message, 'form': form})
                else:
                    with open(f"runr/export/" + filename, 'rb') as excel:
                        data = excel.read()
                        response = HttpResponse(data,
                                                content_type='application/vnd.openxmlformats-'
                                                             'officedocument.spreadsheetml.sheet')
                        response['Content-Disposition'] = f'attachment; filename=' + filename
                        return response


def get_sample(request):
    rscript = open(BASE_DIR / 'runr/rscript_sample.r', "r").read()
    form = RscriptForm(request.POST)

    mutable_script = form.data._mutable
    form.data._mutable = True
    form.data["script"] = rscript
    form.data._mutable = mutable_script

    context = {
        'form': form
    }
    return render(request, 'home.html', context=context)
