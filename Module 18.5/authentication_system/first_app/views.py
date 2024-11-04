from django.shortcuts import render, redirect
from first_app.forms import RegisterForm, LoginForm, CustomChangePassForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'first_app/home.html')

def signupviews(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            Username = form.cleaned_data['username']
            form.save()
            # print(form.cleaned_data)
            messages.success(request, f'{Username} User create successfully')
        else:
            messages.warning(request, 'User information is not valid')
    else:
        form = RegisterForm()
    return render(request, 'first_app/register.html', {'form' : form})

def loginviews(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password= password)
        if user is None:
            messages.warning(request, 'User imformations is not match')
            return redirect('signuppage')
        else:
            login(request, user)
            messages.success(request, f'{username} User login successfully')
            return redirect('profilepage')

    return render(request, 'first_app/login.html', {'form' : form})

@login_required
def profileviews(request):
    return render(request, 'first_app/profile.html')

@login_required
def logoutviews(request):
    logout(request)
    return redirect('signuppage')

@login_required
def passwordchangeviews(request):
    if request.method == 'POST':
        form = CustomChangePassForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User password update successfully')
            update_session_auth_hash(request, request.user)
    else:
        form = CustomChangePassForm(request.user)
    return render(request, 'first_app/password_change.html',{'form' : form})