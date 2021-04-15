from django.contrib.messages.api import set_level
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, ChangePasswordForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('Data:index')
    else:
        return redirect('Administration:login')
def login_request(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('Data:index')
                else:
                    context = {
                        'form':form,
                        'signup':False
                    }
                    messages.warning(request, 'Your Credentials Were Incorrect', extra_tags=['warning',"fas fa-user-slash"])
                    return render(request,'Administration/login.html',context=context)
            else:
                context = {
                        'form':form,
                        'signup':False
                    }
                messages.warning(request, 'Your Credentials Were Incorrect', extra_tags=['warning',"fas fa-user-slash"])
                return render(request,'Administration/login.html',context=context)
        else:
            context = {
                'form':LoginForm(),
                'signup':False
            }
            return render(request,'Administration/login.html',context=context)
    else:
        return redirect('Administration:index')

@login_required
def password_change_request(request):
    if request.method == "POST":
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('Data:index')
        else:
            context = {
                    'form':form,
                    'signup':False
                }
            messages.warning(request, 'Your new password was invalid', extra_tags=['danger',"fas fa-user-times"])
            return render(request,'Administration/changePass.html',context=context)
    else:
        context = {
            'form':ChangePasswordForm(user=request.user),
            'signup':False
        }
        return render(request,'Administration/changePass.html',context=context)

def logout_request(request):
    logout(request)
    return redirect('Administration:index')