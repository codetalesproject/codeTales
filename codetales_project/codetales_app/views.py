from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration, Feedback, ListTrial
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def listdata(request):
    listTrialVariable=ListTrial.objects.all()
    return render(request, 'listdata.html',{'sandc':listTrialVariable})

def profile(request):
    currentUser=request.session['my_session']
    userInfo=Registration.objects.get(Email=currentUser)
    userFullName=userInfo.FullName
    userEmail=userInfo.Email
    return render(request, 'profile.html',{'userFullName':userFullName,'userEmail':userEmail})

def feedback(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        message=request.POST.get("message")
        Feedback(Name=name,Email=email,Phone=phone,Message=message).save()
        return render(request, 'homepage.html')
    else:
        return render(request, 'feedback.html')

def homepage(request):
    return render(request, 'homepage.html')

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
                loginDetails=Registration.objects.get(Email=email,Password=password)
                sessionEmail=loginDetails.Email
                request.session['my_session']=sessionEmail
                return render(request,'homepage.html')
            else:
                error_message = "Invalid credentials. Please try again!"
                return render(request, 'reglog.html', {'error_message': error_message})
    else:
        return render(request,'reglog.html')