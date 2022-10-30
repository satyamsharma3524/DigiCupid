from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    return HttpResponse(render(request, "template/index.html"))

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pswd']
        password2 = request.POST['pswd2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken.")
                return redirect('login')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken.")
                return redirect('login')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
        else:
            messages.info(request, "Password not Matching.")
            return redirect('login')
    return HttpResponse(render(request, "template/login.html"))

def editProfile(request):
    return HttpResponse(render(request, "template/userProfile_edit.html"))

def userProfile(request):
    return HttpResponse(render(request, "template/userProfile.html"))