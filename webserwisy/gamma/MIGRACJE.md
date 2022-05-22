Polecenia dla migracji
======================

Podstawy:

```shell
python manage.py makemigrations
python manage.py showmigrations appname
python manage.py migrate
```

Cofnięcie (tu: do stanu po migracji 006):
```shell
python manage.py migrate appmane 0006
```

Dodanie ręczne pustej migracji:
```shell
python manage.py makemigrations --empty --name nazwa_migracji appname
```

Przykładowa procedura migracji danych
-------------------------------------

- Dodajemy nowe pole z `null=True`
- `makemigrations`
- Dodajemy pustą migrację i robimy w niej uzupełnienie dodanego pola (przez `RunPython`)
- Usuwamy `null=True` z pola
- `makemigrations` (akceptujemy możliwość niespójności)
- `migrate`
