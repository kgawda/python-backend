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