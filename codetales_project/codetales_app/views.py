from django.shortcuts import render
from django.http import HttpResponse
import smtplib
from .models import Registration, Feedback, AdminRegistration
from .models import PyChallenge,PyPuzzle,PyStory,CChallenge,CPuzzle,CStory
# Create your views here.
def index(request):
    return render(request, 'index.html')

# def resetlink(request):
#     if request.method=='POST':
#         email=request.POST.get('email')
#         s=smtplib.SMTP('smtp.gmail.com', 587)
#         s.starttls()
#         s.login("nefsal003@gmail.com", "htxalvzrrkxupspv")
#         message="Click on the link below to reset password"
#     return render(request, 'resetlink.html')

# def resetpassword(request):
#     return render(request, 'resetpassword.html')

def deleteprofile(request,id):
    delid=Registration.objects.get(id=id)
    delid.delete()
    return render(request, 'adminhomepage.html')

def adminprofile(request):
    userProfile=Registration.objects.all()
    return render(request, 'adminprofile.html',{'data':userProfile})

def adminhomepage(request):
    return render(request, 'adminhomepage.html')

def adminfeedback(request):
    fb=Feedback.objects.all()
    return render(request, 'adminfeedback.html',{'fb':fb})

def about(request):
    return render(request, 'about.html')

def clevel(request):
    return render(request, 'clevel.html')

def pylevel(request):
    return render(request, 'pylevel.html')

def profile(request):
    if request.method=="POST":
        if 'submitUpdate' in request.POST:
            id=request.POST.get('id')
            name=request.POST.get('FullName')
            email=request.POST.get('Email')
            updobj=Registration.objects.filter(Email=email)
            if updobj:
                error_message = "Email already in use! Can't Update"
                currentUser=request.session['my_session']
                userInfo=Registration.objects.get(id=currentUser)
                id=userInfo.id
                userFullName=userInfo.FullName
                userEmail=userInfo.Email
                return render(request, 'profileupdate.html',{'id':id,'userFullName':userFullName,
                                                            'userEmail':userEmail,'error_message':error_message})
            else:
                mv=Registration.objects.get(id=id)
                mv.FullName=name
                mv.Email=email
                mv.save()
                currentUser=request.session['my_session']
                userInfo=Registration.objects.get(id=currentUser)
                userFullName=userInfo.FullName
                userEmail=userInfo.Email
                return render(request, 'profile.html',{'userFullName':userFullName,'userEmail':userEmail})
        elif 'cancelUpdate' in request.POST:
            currentUser=request.session['my_session']
            userInfo=Registration.objects.get(id=currentUser)
            userFullName=userInfo.FullName
            userEmail=userInfo.Email
            return render(request, 'profile.html',{'userFullName':userFullName,'userEmail':userEmail})
    else:
        currentUser=request.session['my_session']
        userInfo=Registration.objects.get(id=currentUser)
        userFullName=userInfo.FullName
        userEmail=userInfo.Email
        return render(request, 'profile.html',{'userFullName':userFullName,'userEmail':userEmail})

def profileupdate(request):
    currentUser=request.session['my_session']
    userInfo=Registration.objects.get(id=currentUser)
    id=userInfo.id
    userFullName=userInfo.FullName
    userEmail=userInfo.Email
    return render(request, 'profileupdate.html',{'id':id,'userFullName':userFullName,'userEmail':userEmail})
    
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

def course(request):
    return render(request, 'course.html')

def courses(request):
    return render(request, 'courses.html')

def bookpage(request,corp,level,page):
    if corp=='c':
        cr=CStory.objects.get(Level=level,Page=page)
        storyName='The C Cipher'
    else:
        cr=PyStory.objects.get(Level=level,Page=page)
        storyName='The Python Chronicles'
    title=cr.Title
    data=cr.Content
    prevp=page-1
    nextp=page+1
    p1=(page*2)-1
    p2=page*2
    return render(request, 'bookpage.html',{'title':title,'data':data,'p1':p1,'p2':p2,'story':storyName,
                                            'corp':corp,'level':level,'prev':prevp,'next':nextp})

def reglog(request):
    if(request.method=="POST"):
        if 'signupFormSubmit' in request.POST:
            fullname=request.POST.get("fullname")
            email=request.POST.get("email")
            password=request.POST.get("password")
            regobj=Registration.objects.filter(Email=email)
            if regobj:
                error_message = "Email already in use! Please try another or login."
                return render(request, 'reglog.html', {'error_message': error_message})
            else:
                Registration(FullName=fullname,Email=email,Password=password).save()
                return render(request,'index.html')
        elif 'loginFormSubmit' in request.POST:
            email=request.POST.get("email")
            password=request.POST.get("password")
            logobj=Registration.objects.filter(Email=email,Password=password)
            if logobj:
                loginDetails=Registration.objects.get(Email=email,Password=password)
                sessionID=loginDetails.id
                request.session['my_session']=sessionID
                return render(request,'homepage.html')
            else:
                error_message = "Invalid credentials! Please try again."
                return render(request, 'reglog.html', {'error_message': error_message})
    else:
        return render(request,'reglog.html')
    
def adminreglog(request):
    if(request.method=="POST"):
        if 'signupFormSubmit' in request.POST:
            fullname=request.POST.get("fullname")
            email=request.POST.get("email")
            password=request.POST.get("password")
            regobj=AdminRegistration.objects.filter(Email=email)
            if regobj:
                reg_error_message = "Email already in use! Please try another or login."
                return render(request, 'adminreglog.html', {'reg_error_message': reg_error_message})
            else:
                AdminRegistration(FullName=fullname,Email=email,Password=password).save()
                return render(request,'index.html')
        elif 'loginFormSubmit' in request.POST:
            email=request.POST.get("email")
            password=request.POST.get("password")
            logobj=AdminRegistration.objects.filter(Email=email,Password=password)
            if logobj:
                loginDetails=AdminRegistration.objects.get(Email=email,Password=password)
                sessionID=loginDetails.id
                request.session['my_session']=sessionID
                return render(request,'adminhomepage.html')
            else:
                error_message = "Invalid credentials! Please try again."
                return render(request, 'adminreglog.html', {'error_message': error_message})
    else:
        return render(request,'adminreglog.html')