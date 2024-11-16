from django.urls import path, include
from Album import views
urlpatterns = [
    path('add/', views.AlbumFormviews.as_view(), name='album_list'),
    path('edit/<int:id>/', views.EditViews.as_view(), name='edit_album'),
    path('delete/<int:id>/', views.Deleteviews.as_view(), name='delete_album'),
]
