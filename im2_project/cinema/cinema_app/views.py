from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Genre
from .forms import GenreForm
from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'genres/base.html')

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

def home(request):
    return redirect('genre_list')