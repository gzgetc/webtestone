from django.shortcuts import render
from javaapp.models import *

# Create your views here.


def java(request):

    #javacourse query
    javacourse=JavaCourse.objects.all()

    #javacourse directtitle query
    javadirecttitle=JavaDirectTitle.objects.all()

    content={'jcourse':javacourse,'jdtitle':javadirecttitle}

    return render(request,'javaapp/java.html',content)