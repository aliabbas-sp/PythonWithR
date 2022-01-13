from django.shortcuts import render
from runr.main import *


def index(request):
    return render(request, 'home.html')


def exec_r_func(request):
    superbowlresults = runr()
    tab_class = "table"
    superbowlresults = superbowlresults.replace("<thead>", "<table class=""" + tab_class + ">""")
    return render(request, 'runr.html', {'superbowlresults': superbowlresults})
