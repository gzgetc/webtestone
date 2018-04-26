from django.conf.urls import include, url
from django.contrib import admin
from linuxapp import views

urlpatterns = [
    url('^linux',views.linux,name='linux'),
]