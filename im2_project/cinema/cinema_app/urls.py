from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='test_view'),
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/add/', views.genre_create, name='genre_create'),
    path('genres/edit/<int:pk>/', views.genre_edit, name='genre_update'),  # Match with views
    path('genres/delete/<int:pk>/', views.genre_delete, name='genre_delete'),

     # urlpattern movies
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movies/new/', views.movie_create, name='movie_create'),
    path('movies/<int:pk>/edit/', views.movie_update, name='movie_update'),
    path('movies/<int:pk>/delete/', views.movie_delete, name='movie_delete'),

    # path('home/', views.home, name='home'), 
]


