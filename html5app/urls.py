from django.conf.urls import include, url
from django.contrib import admin
from html5app import views

urlpatterns = [
    url(r'^html5course',views.html5course,name='html5course'),
]