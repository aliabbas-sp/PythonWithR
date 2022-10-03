from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('admin/', admin.site.urls),
    path('pythonwithr_exec', views.exec_rscript, name="pythonwithr_exec"),
    path('example/', views.get_sample, name="example"),
]
