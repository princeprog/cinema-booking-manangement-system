from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='test_view'),
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/add/', views.genre_create, name='genre_create'),
    path('genres/edit/<int:pk>/', views.genre_edit, name='genre_update'),
    path('genres/delete/<int:pk>/', views.genre_delete, name='genre_delete'),

    # URL patterns for movies
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movies/new/', views.movie_create, name='movie_create'),
    path('movies/<int:pk>/edit/', views.movie_update, name='movie_update'),
    path('movies/<int:pk>/delete/', views.movie_delete, name='movie_delete'),

    # URL patterns for cinemas
    path('cinemas/', views.cinema_list, name='cinema_list'),
    path('cinemas/new/', views.cinema_create, name='cinema_create'),
    path('cinemas/<int:pk>/edit/', views.cinema_update, name='cinema_update'),
    path('cinemas/<int:pk>/delete/', views.cinema_delete, name='cinema_delete'),
    path('cinemas/<int:pk>/', views.cinema_detail, name='cinema_detail'),

    # URL patterns for branches
    path('branches/', views.branch_list, name='branch_list'),
    path('branches/new/', views.branch_create, name='branch_create'),
    path('branches/<int:pk>/edit/', views.branch_update, name='branch_update'),
    path('branches/<int:pk>/delete/', views.branch_delete, name='branch_delete'),

    # URL patterns for cinema movies
    path('cinema_movies/', views.cinema_movie_list, name='cinema_movie_list'),
    path('cinema_movies/new/', views.cinema_movie_create, name='cinema_movie_create'),
    path('cinema_movies/<int:pk>/edit/', views.cinema_movie_update, name='cinema_movie_update'),
    path('cinema_movies/<int:pk>/delete/', views.cinema_movie_delete, name='cinema_movie_delete'),

    # URL patterns for seats
    path('seats/', views.seat_list, name='seat_list'),
    path('seats/new/', views.seat_create, name='seat_create'),
    path('seats/<int:pk>/edit/', views.seat_update, name='seat_update'),
    path('seats/<int:pk>/delete/', views.seat_delete, name='seat_delete'),

    # Paths for customer display, delete, update, read
    path('signup/', views.signup_view, name='signup'),
    path('customer-success/', views.customer_success, name='customer_success'),
    path('update-customer/<int:customer_id>/', views.update_customer, name='update_customer'),
    path('delete-customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),

    # Paths for booking
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/create/', views.create_booking, name='create_booking'),
    path('bookings/<int:booking_id>/update/', views.update_booking, name='update_booking'),
    path('bookings/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
    path('bookings/<int:cinema_movie_id>/book/', views.booking, name='booking'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('payment/<int:cinema_movie_id>/', views.payment, name='payment'),

    # User side
    path('signup/', views.signup_view, name='signupform'),
    path('login/', views.login_view, name='loginform'),
    path('', views.landing_page, name='landing_page'),
    path('home/', views.home_page, name='home_page'),

    # Admin dashboard
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Admin login and signup
    path('admin-login/', views.login_view, name='admin_login'),
    path('admin-signup/', views.admin_signup, name='admin_signup'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),

    # Showtimes
    path('showtimes/', views.showtimes, name='showtimes'),
]