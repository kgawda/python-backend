from django.shortcuts import render
from .models import Movie

def home(request):
    context = {
        'highlights':
            {Movie.objects.first(): Movie.objects.first().cinemas_that_play_it()},
    }
    return render(request, "cinemas/index.html", context)
