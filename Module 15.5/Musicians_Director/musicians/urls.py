from django.contrib import admin
from django.urls import path,include

from .import views
urlpatterns = [
    # path('data/', views.musician, name="musician"),/\
    path('form/', views.Musician_Form, name="musicianpage"),
    path('edit/<int:id>', views.Edit_musician, name="editmusician")
]