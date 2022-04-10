import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Book, Author
from .forms import AddBookForm, BookForm_ModelForm

def home(request):
    browser = request.headers['User-Agent'].split()[-1]
    books = Book.objects.all()
    context = {
        'title': "Pierwsza strona",
        'time': datetime.datetime.now().strftime('%H:%M:%S'),
        'browser': browser,
        'books': books,
    }

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

def add_book(request):
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            author = Author.objects.get(name=form.cleaned_data["author_name"])
            book = Book(
                title=form.cleaned_data["title"],
                author=author,
                description=form.cleaned_data["description"]
            )
            book.save()
            messages.success(request, "Dodano książkę!")  # from django.contrib import messages
            return HttpResponseRedirect(reverse('book', args=(book.id,)))
    else:
        form = AddBookForm()

    return render(request, 'library/add_book.html', {'form': form})

def add_book_modelform(request):
    if request.method == "POST":
        form = BookForm_ModelForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, "Dodano książkę!")  # from django.contrib import messages
            return HttpResponseRedirect(reverse('book', args=(book.id,)))
    else:
        form = BookForm_ModelForm()
    return render(request, 'library/add_book.html', {'form': form})