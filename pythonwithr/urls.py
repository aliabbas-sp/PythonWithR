from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("runr/", views.exec_r_func, name="runr"),
    path('', views.index, name="home"),
]
