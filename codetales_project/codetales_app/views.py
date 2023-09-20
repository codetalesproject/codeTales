from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def price(request):
    return render(request, 'price.html')
def service(request):
    return render(request, 'service.html')
def login(request):
    if(request.method=="POST"):
        uname=request.POST.get("username")
        pwd=request.POST.get("password")
        Login(UserName=uname,Password=pwd).save()
        return render(request,'index.html')
    else:
        return render(request,'login.html')
