from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from django.contrib import auth
from django.contrib.auth import authenticate 


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return render (request,'registration/login.html/', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'registration/login.html/')



