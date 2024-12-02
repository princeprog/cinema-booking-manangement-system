from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from .models import Genre, Movie, Branch, Cinema, Cinema_Movie, Customer, Seats, Booking
from .forms import GenreForm, MovieForm, BranchForm, CinemaForm, CinemaMovieForm, CustomerForm, BookingForm, CustomerSignupForm, SeatForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
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

def test_view(request):
    return render(request, 'templates/base.html')

def home_page(request):
    return render(request, 'home.html')

def landing_page(request):
    cinemas = Cinema.objects.all()
    return render(request, 'landing.html', {'cinemas': cinemas})

def admin_dashboard(request):
    return render(request, 'admin/admin.html')

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

# Movie CRUD
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'admin/movies_admin.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    data = {
        'title': movie.title,
        'duration': movie.duration,
        'description': movie.description,
        'genre': movie.genre.name,
    }
    return JsonResponse(data)

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    genres = Genre.objects.all()
    return render(request, 'admin/add_movies_admin.html', {'form': form, 'genres': genres})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    genres = Genre.objects.all()
    return render(request, 'admin/update_movie_admin.html', {'form': form, 'genres': genres})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'admin/movies_admin.html', {'movie': movie})

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
    branches = Branch.objects.all()
    return render(request, 'cinemas/cinema_form.html', {'form': form, 'branches': branches})

def cinema_update(request, pk):
    cinema = get_object_or_404(Cinema, pk=pk)
    if request.method == 'POST':
        form = CinemaForm(request.POST, instance=cinema)
        if form.is_valid():
            form.save()
            return redirect('cinema_list')
    else:
        form = CinemaForm(instance=cinema)
    branches = Branch.objects.all()
    return render(request, 'cinemas/cinema_form.html', {'form': form, 'branches': branches})

def cinema_delete(request, pk):
    cinema = get_object_or_404(Cinema, pk=pk)
    if request.method == 'POST':
        cinema.delete()
        return redirect('cinema_list')
    return render(request, 'cinemas/cinema_confirm_delete.html', {'cinema': cinema})

def cinema_detail(request, pk):
    cinema = get_object_or_404(Cinema, pk=pk)
    data = {
        'cinema_name': cinema.cinema_name,
        'branch': cinema.branch.branch_name,
    }
    return JsonResponse(data)

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
    movies = Movie.objects.all()
    cinemas = Cinema.objects.all()
    return render(request, 'cinemas/cinema_movie_form.html', {'form': form, 'movies': movies, 'cinemas': cinemas})

def cinema_movie_update(request, pk):
    cinema_movie = get_object_or_404(Cinema_Movie, pk=pk)
    if request.method == 'POST':
        form = CinemaMovieForm(request.POST, instance=cinema_movie)
        if form.is_valid():
            form.save()
            return redirect('cinema_movie_list')
    else:
        form = CinemaMovieForm(instance=cinema_movie)
    movies = Movie.objects.all()
    cinemas = Cinema.objects.all()
    return render(request, 'cinemas/cinema_movie_form.html', {'form': form, 'movies': movies, 'cinemas': cinemas})
def cinema_movie_delete(request, pk):
    cinema_movie = get_object_or_404(Cinema_Movie, pk=pk)
    if request.method == 'POST':
        cinema_movie.delete()
        return redirect('cinema_movie_list')
    return render(request, 'cinemas/cinema_movie_confirm_delete.html', {'cinema_movie': cinema_movie})

# Sign up view
def signup_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.password = form.cleaned_data['password']
            customer.save()
            return redirect('loginform')
    else:
        form = CustomerForm()
    return render(request, 'user-side/signupform.html', {'form': form})

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

# Booking views
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'cinema_app/booking_list.html', {'bookings': bookings})

# Create view
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'cinema_app/booking_form.html', {'form': form})

# Update view
def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'cinema_app/booking_form.html', {'form': form})

# Delete view
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'booking/booking_delete.html', {'booking': booking})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            customer = Customer.objects.get(username=username)
            if customer.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('landing_page')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid username or password'})
    return render(request, 'admin_login.html')

@login_required
def profile_view(request):
    user = request.user
    # profile_picture = user.profile.profile_picture  # Assuming you have a profile model with a profile_picture field
    bookings = Booking.objects.all()
    # return render(request, 'cinema_app/booking_list.html', {'bookings': bookings})

    context = {
        'user': user,
        # 'profile_picture': profile_picture,
        'bookings': bookings,
    }
    return render(request, 'user-side/profile.html', {'bookings': bookings})

#  Showtimes/User side
def showtime(request):
    cinema_movies = Cinema_Movie.objects.all()
    return render(request, 'user-side/showtimes.html', {'cinema_movies': cinema_movies})

# Book now User Side
def booknow(request):
    return render(request, 'user-side/booknow.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            customer = Customer.objects.get(username=username)
            if customer.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('home_page')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid username or password'})
    return render(request, 'admin_login.html')

def admin_signup(request):
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                form.add_error('confirm_password', 'Passwords do not match')
            elif User.objects.filter(username=username).exists():
                form.add_error('username', 'Username is already taken')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                customer = form.save(commit=False)
                customer.password = user.password  # Save the hashed password
                customer.save()
                return redirect('admin_login')
    else:
        form = CustomerSignupForm()
    return render(request, 'admin_signup.html', {'form': form})

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

def showtimes(request):
    cinema_movies = Cinema_Movie.objects.select_related('movie_ID', 'cinema_ID').all()
    return render(request, 'showtimes.html', {'cinema_movies': cinema_movies})

def seat_list(request):
    seats = Seats.objects.all()
    if request.method == 'POST':
        # Automatically generate the next seat number
        last_seat = Seats.objects.order_by('seat_no').last()
        next_seat_no = last_seat.seat_no + 1 if last_seat else 1
        seat = Seats(seat_no=next_seat_no)
        seat.save()
        return redirect('seat_list')
    return render(request, 'seats/seat_list.html', {'seats': seats})

def seat_create(request):
    if request.method == 'POST':
        form = SeatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seat_list')
    else:
        form = SeatForm()
    return render(request, 'seats/seat_form.html', {'form': form})

def seat_update(request, pk):
    seat = get_object_or_404(Seats, pk=pk)
    if request.method == 'POST':
        form = SeatForm(request.POST, instance=seat)
        if form.is_valid():
            form.save()
            return redirect('seat_list')
    else:
        form = SeatForm(instance=seat)
    return render(request, 'seats/seat_form.html', {'form': form})

def seat_delete(request, pk):
    seat = get_object_or_404(Seats, pk=pk)
    if request.method == 'POST':
        seat.delete()
        return redirect('seat_list')
    return render(request, 'seats/seat_confirm_delete.html', {'seat': seat})

def booking(request, cinema_movie_id):
    cinema_movie = get_object_or_404(Cinema_Movie, pk=cinema_movie_id)
    seats = Seats.objects.all()
    if request.method == 'POST':
        showtime = request.POST['showtime']
        seat = request.POST['seat']
        # Handle booking logic here
        return redirect('booking_success')
    return render(request, 'booking.html', {'cinema_movie': cinema_movie, 'seats': seats})

def booking_success(request):
    return render(request, 'booking_success.html')

def payment(request, cinema_movie_id):
    cinema_movie = get_object_or_404(Cinema_Movie, pk=cinema_movie_id)
    seats = Seats.objects.all()
    if request.method == 'POST':
        seat_id = request.POST.get('seat')
        payment_method = request.POST.get('payment_method')
        customer = Customer.objects.get(username=request.user.username)
        seat = get_object_or_404(Seats, pk=seat_id)
        booking = Booking(
            cinema_movie_id=cinema_movie,
            customer_id=customer,
            seat_no=seat,
            date=timezone.now().date(),
            time=timezone.now().time()
        )
        booking.save()
        return redirect('booking_success')
    return render(request, 'payment.html', {'cinema_movie': cinema_movie, 'seats': seats})

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')