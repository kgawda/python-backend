from django.shortcuts import render
from .models import Movie

def home(request):
    context = {
        'movies': Movie.objects.all()
    }
    return render(request, "cinemas/index.html", context)

