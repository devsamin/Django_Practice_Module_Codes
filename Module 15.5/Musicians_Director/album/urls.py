from django.contrib import admin
from django.urls import path,include

from .import views
urlpatterns = [
    path('form/', views.Album_Form, name="albumpage"),
    path('edit/<int:id>', views.Edit_album, name='editalbum'),
    path('delete/<int:id>', views.delete_album, name='delalbum'),
]