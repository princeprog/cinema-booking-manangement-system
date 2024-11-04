from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/add/', views.genre_create, name='genre_create'),
    path('genres/edit/<int:pk>/', views.genre_edit, name='genre_update'),  # Match with views
    path('genres/delete/<int:pk>/', views.genre_delete, name='genre_delete'),
]


