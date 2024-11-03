from django.urls import path
from .views import create_customer, customer_success, update_customer, delete_customer


urlpatterns = [
    path('create-customer/', create_customer, name='create_customer'),
    path('customer-success/', customer_success, name='customer_success'),
    path('update-customer/<int:customer_id>/', update_customer, name='update_customer'),
    path('delete-customer/<int:customer_id>/', delete_customer, name='delete_customer'),
]
