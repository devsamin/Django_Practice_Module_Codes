from django.urls import path, include
from musician import views
urlpatterns = [
    path('add', views.MusicianFormviews.as_view(), name="musician_list")
]
