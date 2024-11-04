from django import forms
from .models import Genre, Movie, Branch, Cinema, Cinema_Movie

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter genre name'}),
        }

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'duration', 'description', 'genre']

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['branch_name']

class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ['cinema_name', 'branch']

class CinemaMovieForm(forms.ModelForm):
    class Meta:
        model = Cinema_Movie
        fields = ['movie_ID', 'cinema_ID', 'showtimes', 'branch']
