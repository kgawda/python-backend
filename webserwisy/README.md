Tworzenie nowego projektu w Django
----------------------------------

Instalacja paczki Django (najlepiej w virtualenv):
```shell
pip install django
# ewentualnie aktualizacja:
pip install -U django
```

Tworzenie nowego projektu:
```shell
django-admin startproject alpha
cd alpha
python manage.py runserver
# Ctrl+C
python manage.py startapp library
# do alpha/settings.py w INSTALLED_APPS dopisujemy 'library'
# do alpha/urls.py dodajemy import library.views 
#    i w urlpaterns dodajemy path('', library.views.home),
# dopisujemy funkcję home w library/views.py
```

Dodaliśmy modele

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py shell
```

```python
from library.models import Author, Book
adam = Author(name="Adam Mickiewicz")
adam.save()

pantadeusz = Book(title="Pan Tadeusz", description="...", author=adam)
pantadeusz.save()
pantadeusz.author.name

Book.objects.all()  # szystkie książki
adam.book_set.all()  # wszystkie książki Adama

# znajdź wszystkie Book w bazie, które mają takie id lub tytuł
Book.objects.filter(id=1)
Book.objects.filter(title="Pan Tadeusz")

# znajdź pojedynczy Book w bazie, który ma taki id lub tytuł
Book.objects.get(id=1)
Book.objects.get(title="Pan Tadeusz")
```