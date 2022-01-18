from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('runr/', views.exec_rscript, name="runr"),
    path('example/', views.get_sample, name="example"),
]
