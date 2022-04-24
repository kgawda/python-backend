from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Cinema(models.Model):
    name = models.CharField(max_length=100)
    seats = models.PositiveSmallIntegerField(validators=[MinValueValidator(10)])

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    minimum_age = models.PositiveSmallIntegerField(validators=[MaxValueValidator(21)])

    def __str__(self):
        return self.title

    def cinemas_that_play_it(self):
        return Cinema.objects.filter(projection__movie=self)

    # Do omówienia: Cinema.objects.filter(projection__movie__title="Chłopaki nie płaczą").filter(projection__movie__minimum_age__lt=8)

class Projection(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField()
    published = models.BooleanField()
    tickets_available = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.movie.title} at {self.cinema.name} on {self.date.strftime('%d.%m.%Y %H:%M:%S')}"
