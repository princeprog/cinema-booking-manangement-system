from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm

def create_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_success') 
    else:
        form = CustomerForm()
    
    return render(request, 'cinema_app/create_customer.html', {'form': form})


def customer_success(request):
    customers = Customer.objects.all()
    return render(request, 'cinema_app/customer_success.html', {'customers': customers})

def update_customer(request, customer_id):
    customer = get_object_or_404(Customer, customer_id=customer_id) 
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_success')  
    else:
        form = CustomerForm(instance=customer)
    
    return render(request, 'cinema_app/update_customer.html', {'form': form})


def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_success')
    return render(request, 'cinema_app/delete_customer.html', {'customer': customer})  

