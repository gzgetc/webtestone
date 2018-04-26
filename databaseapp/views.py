from django.shortcuts import render
from databaseapp.models import *

# Create your views here.


def databsecourse(request):

    #datacourse query
    datacourse=DataCourse.objects.all()

    #datacourse directtitle query
    datadirecttitle=DataDirectory.objects.all()

    content={'dcourse':datacourse,'ddtitle':datadirecttitle}

    return render(request,'databaseapp/databasecourse.html',content)