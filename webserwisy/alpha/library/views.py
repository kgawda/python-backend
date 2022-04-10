import datetime

from django.shortcuts import render, get_object_or_404

from .models import Book, Author

def home(request):
    browser = request.headers['User-Agent'].split()[-1]
    books = Book.objects.all()
    context = {
        'title': "Pierwsza strona",
        'time': datetime.datetime.now().strftime('%H:%M:%S'),
        'browser': browser,
        'books': books,
    }
    #print(request.path, request.method, request.META, request.headers)
    print(request.method, request.POST)
    return render(request, 'library/index.html', context)

def book(request, book_id):
    #book = Book.objects.get(id=book_id)
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library/book.html', {'book': book})

def author(request, author_id):
    #author = Author.objects.get(id=author_id)
    author = get_object_or_404(Author, id=author_id)
    books = author.book_set.all()
    return render(request, 'library/author.html', {'author': author, 'books': books})