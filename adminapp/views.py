from django.shortcuts import render

# Create your views here.

def userlogin(request):
    return render(request,'adminapp/userlogin.html')

def userregister(request):
    return render(request,'adminapp/userregister.html')