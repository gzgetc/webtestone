from django.shortcuts import render
from pythonapp.models import *

# Create your views here.



def pyth(request):
    # pythoncourse query
    pythoncourse = PythonCourse.objects.all()

    # pythoncourse directtitle query
    pythondirecttitle = PythonDirectTitle.objects.all()

    content = {'pcourse': pythoncourse, 'pdtitle': pythondirecttitle}

    return render(request, 'pythonapp/python.html', content)