from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    movieId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Branch(models.Model):
    branch_ID = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=100)

    def __str__(self):
        return self.branch_name

class Cinema(models.Model):
    cinema_ID = models.AutoField(primary_key=True)
    cinema_name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.cinema_name

class Cinema_Movie(models.Model):
    movie_ID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema_ID = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    showtimes = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.movie_ID.title} at {self.cinema_ID.cinema_name}"

class Customer(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    customer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)  
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.PositiveBigIntegerField()
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return self.username

class Seats(models.Model):  
    seat_no = models.AutoField(primary_key=True)

class Booking(models.Model):
    booking_Id = models.AutoField(primary_key=True)
    cinema_movie_id = models.ForeignKey(Cinema_Movie, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seat_no = models.ForeignKey(Seats, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()