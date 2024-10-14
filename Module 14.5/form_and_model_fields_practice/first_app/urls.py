from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.contact1, name="contact1page"),
    path('contact2/', views.contact2, name="contact2page"),
]