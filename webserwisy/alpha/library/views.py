from django.shortcuts import render


def home(request):
    context = {'title': "Pierwsza strona", 'dump': request}
    #print(request.path, request.method, request.META, request.headers)
    return render(request, 'library/index.html', context)
