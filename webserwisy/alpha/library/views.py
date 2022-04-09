from django.shortcuts import render
import datetime


def home(request):
    browser = request.headers['User-Agent'].split()[-1]
    context = {
        'title': "Pierwsza strona",
        'time': datetime.datetime.now().strftime('%H:%M:%S'),
        'browser': browser,
    }
    print(request.path, request.method, request.META, request.headers)
    return render(request, 'library/index.html', context)
