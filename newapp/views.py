from django.shortcuts import render
from .forms import UserForm,AuthForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django import forms
from django.contrib import messages




# Create your views here.
def RegisterView(request):

    registered = False
    if request.method == 'POST':
        user = UserForm(request.POST)
        if user.is_valid():
            username = user.cleaned_data['username']
            password = user.cleaned_data['password']
            User.objects.create_user(username=username,password=password)
            registered = True
            return render(request,'register.html',{'form':user,'registered':registered})
    else:
        user = UserForm()

    return render(request,'register.html',{'form':user,'registered':registered})


def HomeView(request):
    return render(request,'base.html')

current_user = ''
def LoginView(request):

    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                auth = authenticate(username=username,password=password) 
                if auth:             
                    login(request,auth)                               
                    return render(request,'base.html')          
        else:
            
            form = AuthForm()

        current_user = request.user.username 
    
    else:
        return render(request,'base.html')


    #current_user = request.user.username
    print(current_user)
    return render(request,'login.html',{'form':form})


def snippet(request):
    return render(request,'snippet.html')