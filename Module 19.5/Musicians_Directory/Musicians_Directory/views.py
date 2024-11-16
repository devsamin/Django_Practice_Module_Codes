from typing import Any
from django.shortcuts import render, redirect
from Album.models import AlbumModel
from django.views.generic import CreateView
from django.contrib.auth.models import User
from Musicians_Directory.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic import ListView

class homeviews(ListView):
    model = AlbumModel
    template_name = 'home.html'
    context_object_name = 'data' # album model er all object k nea context e patidibe


class UserRegisterviews(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'registerform.html'
    success_url = reverse_lazy('register_page')

    def form_valid(self, form):
        #save the user and with has password
        user = form.save(commit = False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(self.request, 'User register successfully')
        return super().form_valid(form)

class UserLoginviews(LoginView):
    template_name = 'login.html'
    # form_class = UserloginForm
    # success_url = reverse_lazy('homepage')
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        messages.success(self.request, 'User login successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'User information not valid')
        return super().form_invalid(form)

def userlogout(request):
    logout(request)
    return redirect('login_page')