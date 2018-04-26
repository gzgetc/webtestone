from django.conf.urls import include, url
from django.contrib import admin
from javaapp import views

urlpatterns = [
    url('^java',views.java,name='java'),
]