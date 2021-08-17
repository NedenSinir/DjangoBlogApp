from user.forms import LoginFrom, RegisterForm
from django.shortcuts import redirect, render
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as autoLogin,logout as autoLogout
from django.contrib import messages




def login(request):
    form=LoginFrom(request.POST or None)
    context={
        "form":form
    }

    if form.is_valid():
        username= form.cleaned_data.get("username")
        password= form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user != None:
            messages.success(request,"Giris Basarili")
            autoLogin(request,user)
            return redirect("index")
        else:
            messages.info(request,"Boyle bir hesap bulunmamakta")
            return render(request,"login.html",context)
    return render(request,"login.html",context)




def logout(request):

    autoLogout(request)
    messages.success(request,"Basariyla Cıkıs yaptiniz")

    return redirect("index")



def register(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username1")
        password= form.cleaned_data.get("password")
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        autoLogin(request,newUser)
        messages.success(request,"Hesap basariyla olusturldu...")
        return redirect("index")
    else:
        context={
        "formm":form,
        }
        return render(request,"register.html",context)