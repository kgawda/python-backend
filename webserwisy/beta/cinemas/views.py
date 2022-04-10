from django.shortcuts import render

def home(request):
    return render(request, "cinemas/index.html", {})
