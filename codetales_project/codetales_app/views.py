from django.shortcuts import render, redirect
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

def adminlogin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        logobj=AdminRegistration.objects.filter(UserName=username,Password=password)
        if logobj:
            loginDetails=AdminRegistration.objects.get(UserName=username,Password=password)
            sessionID=loginDetails.id
            request.session['my_session']=sessionID
            return redirect('adminhomepage')
        else:
            error_message = "Invalid credentials! Please try again."
            return render(request, 'adminlogin.html', {'error_message': error_message})
    else:
        return render(request, 'adminlogin.html')

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

def plevel(request):
    return render(request, 'plevel.html')

def profile(request):
    if request.method=="POST":
        if 'submitUpdate' in request.POST:
            id=request.POST.get('id')
            name=request.POST.get('FullName')
            email=request.POST.get('Email')
            currentUserID=request.session['my_session']
            currentUserInfo=Registration.objects.get(id=currentUserID)
            currentUserEmail=currentUserInfo.Email
            flag = 0 if email == currentUserEmail else 1
            updobj=False
            if flag:
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
                return redirect('profile')
        elif 'cancelUpdate' in request.POST:
            return redirect('profile')
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
        return redirect('homepage')
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
        try:
            cr=CStory.objects.get(Level=level,Page=page)
            storyName='The C Cipher'
        except CStory.DoesNotExist:
            redirectpage=corp+"level"
            return redirect(redirectpage)
    elif corp=='p':
        try:
            cr=PyStory.objects.get(Level=level,Page=page)
            storyName='The Python Chronicles'
        except PyStory.DoesNotExist:
            redirectpage=corp+"level"
            return redirect(redirectpage)
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
                return redirect('reglog')
        elif 'loginFormSubmit' in request.POST:
            email=request.POST.get("email")
            password=request.POST.get("password")
            logobj=Registration.objects.filter(Email=email,Password=password)
            if logobj:
                loginDetails=Registration.objects.get(Email=email,Password=password)
                sessionID=loginDetails.id
                request.session['my_session']=sessionID
                return redirect('homepage')
            else:
                error_message = "Invalid credentials! Please try again."
                return render(request, 'reglog.html', {'error_message': error_message})
    else:
        return render(request,'reglog.html')