from django.conf.urls import include, url
from django.contrib import admin
from adminapp import views

urlpatterns = [
    url('^userlogin',views.userlogin,name='userlogin'),
    url('^userregister',views.userregister,name='userregister'),
]