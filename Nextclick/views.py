from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render(request,"home.html")

def Registration(request):
    return render(request,"registration.html")

def Login(request):
    return render(request,"login.html")
