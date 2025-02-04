from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def Register(request):
    if request == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        new_user = User.objects.create_user(name=name,email=email,password=password,cpassword=cpassword)
        new_user.save()
    return render(request,"app/register.html")

# def RegisterPage(request):


def Index(request):
    return render(request,"app/index.html")

def Login(request):
    return render(request,"app/login.html")

