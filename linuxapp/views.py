from django.shortcuts import render
from linuxapp.models import *

# Create your views here.



def linux(request):
    # pythoncourse query
    linuxcourse = LinuxCourse.objects.all()

    # pythoncourse directtitle query
    linuxdirecttitle = LinuxDirectTitle.objects.all()

    content = {'lcourse': linuxcourse, 'ldtitle': linuxdirecttitle}

    return render(request, 'linuxapp/linux.html', content)