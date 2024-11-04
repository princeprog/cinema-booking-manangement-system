from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Genre
from .forms import GenreForm
from django.shortcuts import render
from .models import Movie
from .forms import MovieForm
from .models import Branch, Cinema, Cinema_Movie
from .forms import BranchForm, CinemaForm, CinemaMovieForm
from .models import Customer
from .forms import CustomerForm
# Create your views here.

def test_view(request):
    return render(request, 'templates/base.html')

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genres/genre_list.html', {'genres': genres})


def genre_create(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre_list')  
    else:
        form = GenreForm()
    return render(request, 'genres/genre_form.html', {'form': form})


def genre_edit(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm(instance=genre)
    return render(request, 'genres/genre_form.html', {'form': form})


def genre_delete(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        genre.delete()
        return redirect('genre_list')
    return render(request, 'genres/genre_confirm_delete.html', {'genre': genre})

# def home(request):
#     return redirect('genre_list')

# MOVIE CRUD
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', pk=pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})

def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'branch/branch_list.html', {'branches': branches})

def branch_create(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    else:
        form = BranchForm()
    return render(request, 'branch/branch_form.html', {'form': form})

def branch_update(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    else:
        form = BranchForm(instance=branch)
    return render(request, 'branch/branch_form.html', {'form': form})

def branch_delete(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    if request.method == 'POST':
        branch.delete()
        return redirect('branch_list')
    return render(request, 'branch/branch_confirm_delete.html', {'branch': branch})

def cinema_list(request):
    cinemas = Cinema.objects.all()
    return render(request, 'cinemas/cinema_list.html', {'cinemas': cinemas})

def cinema_create(request):
    if request.method == 'POST':
        form = CinemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cinema_list')
    else:
        form = CinemaForm()
    return render(request, 'cinemas/cinema_form.html', {'form': form})

# Cinema_Movie Views
def cinema_movie_list(request):
    cinema_movies = Cinema_Movie.objects.all()
    return render(request, 'cinemas/cinema_movie_list.html', {'cinema_movies': cinema_movies})

def cinema_movie_create(request):
    if request.method == 'POST':
        form = CinemaMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cinema_movie_list')
    else:
        form = CinemaMovieForm()
    return render(request, 'cinemas/cinema_movie_form.html', {'form': form})


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