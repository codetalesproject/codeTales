from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration
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
def reglog(request):
    if(request.method=="POST"):
        fullname=request.POST.get("fullname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Registration(FullName=fullname,Email=email,Password=password).save()
        return render(request,'reglog.html')
    else:
        return render(request,'reglog.html')