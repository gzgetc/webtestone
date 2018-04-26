from django.shortcuts import render
from html5app.models import *

# Create your views here.


def html5course(request):

    #datacourse query
    html5course=Html5Course.objects.all()

    #datacourse directtitle query
    html5directtitle=Html5Directory.objects.all()

    content={'hcourse':html5course,'hdtitle':html5directtitle}

    return render(request,'html5app/html5course.html',content)