from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration, Feedback
# Create your views here.
def index(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        message=request.POST.get("message")
        Feedback(Name=name,Email=email,Phone=phone,Message=message).save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def profile(request):
    return render(request, 'profile.html')
def contact(request):
    return render(request, 'contact.html')
def price(request):
    return render(request, 'price.html')
def service(request):
    return render(request, 'service.html')
def reglog(request):
    if(request.method=="POST"):
        if 'sup' in request.POST:
            fullname=request.POST.get("fullname")
            email=request.POST.get("email")
            password=request.POST.get("password")
            Registration(FullName=fullname,Email=email,Password=password).save()
            return render(request,'index.html')
        elif 'loin' in request.POST:
            email=request.POST.get("email")
            password=request.POST.get("password")
            logobj=Registration.objects.filter(Email=email,Password=password)
            if logobj:
                return render(request,'index.html')
            else:
                error_message = "Invalid credentials. Please try again!"
                return render(request, 'reglog.html', {'error_message': error_message})
    else:
        return render(request,'reglog.html')