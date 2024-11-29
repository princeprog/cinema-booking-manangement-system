from django import forms
from .models import Genre, Movie, Branch, Cinema, Cinema_Movie, Customer, Booking, Seats

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
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie title'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter duration in minutes'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter movie description'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
        }

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['branch_name']
        widgets = {
            'branch_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch name'}),
        }

class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ['cinema_name', 'branch']
        widgets = {
            'cinema_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter cinema name'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
        }

class CinemaMovieForm(forms.ModelForm):
    class Meta:
        model = Cinema_Movie
        fields = ['movie_ID', 'cinema_ID', 'showtimes']
        widgets = {
            'movie_ID': forms.Select(attrs={'class': 'form-control'}),
            'cinema_ID': forms.Select(attrs={'class': 'form-control'}),
            'showtimes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter showtimes'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'username', 'password', 'age', 'address', 'role']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['cinema_movie_id', 'customer_id', 'seat_no', 'date', 'time']
        widgets = {
            'cinema_movie_id': forms.Select(attrs={'class': 'form-control'}),
            'customer_id': forms.Select(attrs={'class': 'form-control'}),
            'seat_no': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter time'}),
        }

class CustomerSignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))

    class Meta:
        model = Customer
        fields = ['username', 'firstname', 'lastname', 'age', 'address', 'password', 'confirm_password', 'role']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }

class SeatForm(forms.ModelForm):
    class Meta:
        model = Seats
        fields = ['seat_no']
        widgets = {
            'seat_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter seat number'}),
        }