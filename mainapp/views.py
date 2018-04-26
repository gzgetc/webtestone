from django.shortcuts import render
from mainapp.models import *
from django.http import HttpResponse
from django.conf import settings
import os
# Create your views here.

def index(request):

    #pnotolbum make data
    photolbumone = PhotoLbum.objects.filter(imgorder=1)
    photolbumtwo = PhotoLbum.objects.filter(imgorder=2)
    photolbumthree = PhotoLbum.objects.filter(imgorder=3)
    photolbumfour = PhotoLbum.objects.filter(imgorder=4)
    #photolbum end

    #photodescrib make data
    photodescribone=PhotoDescrib.objects.filter(imgorder=1)
    photodescribtwo=PhotoDescrib.objects.filter(imgorder=2)
    photodescribthree=PhotoDescrib.objects.filter(imgorder=3)
    photodescribfour=PhotoDescrib.objects.filter(imgorder=4)
    photodescribfives=PhotoDescrib.objects.filter(imgorder=5)
    photodescribsix=PhotoDescrib.objects.filter(imgorder=6)
    photodescribseven=PhotoDescrib.objects.filter(imgorder=7)
    photodescribeight=PhotoDescrib.objects.filter(imgorder=8)
    photodescribnine=PhotoDescrib.objects.filter(imgorder=9)
    photodescribten=PhotoDescrib.objects.filter(imgorder=10)
    photodescribeleven=PhotoDescrib.objects.filter(imgorder=11)
    photodescribtwelve=PhotoDescrib.objects.filter(imgorder=12)
    #photodescrib end

    headcaption=HeadCaption.objects.all()
    content={'hcaption':headcaption,
             #photolbum start
             'photolbumone':photolbumone,
             'photolbumtwo':photolbumtwo,
             'photolbumthree':photolbumthree,
             'photolbumfour':photolbumfour,
             #photolbum end

             #photodescrib start
             'photodescribone':photodescribone,
             'photodescribtwo':photodescribtwo,
             'photodescribthree':photodescribthree,
             'photodescribfour':photodescribfour,
             'photodescribfives':photodescribfives,
             'photodescribsix':photodescribsix,
             'photodescribseven':photodescribseven,
             'photodescribeight':photodescribeight,
             'photodescribnine':photodescribnine,
             'photodescribten':photodescribten,
             'photodescribeleven':photodescribeleven,
             'photodescribtwelve':photodescribtwelve,
             #photodescrib end


             }
    return render(request,'mainapp/index.html',content)



