from django.conf.urls import include, url
from django.contrib import admin
from databaseapp import views

urlpatterns = [
    url(r'^database',views.databsecourse,name='databasecourse'),
]