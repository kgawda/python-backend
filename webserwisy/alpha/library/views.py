from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Witajcie na stronie zbudowanej za pomocą widoku")
