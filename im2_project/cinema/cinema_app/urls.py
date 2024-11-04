
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

    path('branches/', views.branch_list, name='branch_list'),
    path('branches/new/', views.branch_create, name='branch_create'),
    path('branches/<int:pk>/edit/', views.branch_update, name='branch_update'),
    path('branches/<int:pk>/delete/', views.branch_delete, name='branch_delete'),

    path('cinemas/', views.cinema_list, name='cinema_list'),
    path('cinemas/new/', views.cinema_create, name='cinema_create'),

    path('cinema_movies/', views.cinema_movie_list, name='cinema_movie_list'),
    path('cinema_movies/new/', views.cinema_movie_create, name='cinema_movie_create'),
]


