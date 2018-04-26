from django.conf.urls import include, url
from django.contrib import admin
from pythonapp import views

urlpatterns = [
    url('^pyth',views.pyth,name='pyth'),
]
