Stringi (str)
#############

`s.upper()` 	- zmienia wszystkie litery na wielkie
`assert "Ala ma kota".upper() == "ALA MA KOTA"`

`s.lower()`	- zmienia wszystkie litery na małe

`s.replace(old, new)` - zastępuje każde wystąpienie napisu old napisem new

`s.strip()` 	- usuwa początkowe i końcowe białe znaki (spacje itp)

`s.split()`	- dzieli napis na poszczególne słowa, wynikiem jest lista słów

`s.splitlines()`  - dzieli wielo-linijkowy napis na linijki, wynikiem jest lista linijek 
```python
s = """Linia 1
Linia 2
Ostatnia linia."""
assert s.splitlines() == ["Linia 1", "Linia 2", "Ostatnia linia."]
```

`s.join(lista_slow)`	- scala napisy z listy lista_slow w jeden napis, łącznikiem jest s
`assert " - ".join(["Warszawa", "Monachium", "Nowy Jork"]) == "Warszawa - Monachium - Nowy Jork"`

`s.count(sub)` 	- zlicza wystąpienie napisu sub w napisie s

`s.index(sub)`	- podaje pozycję, na której zaczyna się napis sub w napisie s (jeśli nie znajdzie zwraca błąd)

`s.find(sub)`		- jak index tylko jeśli nie znajdzie, to zwraca -1

`s.find(sub, start, end)` - find z podaniem opcjonalnych argumentów, wyszukuje w s[start:end]

`s.startswith(sub)` - sprawdza, czy s zaczyna się od napisu sub

`s.isdigit()` 	- sprawdza czy wszystkie znaki są cyframi

`s.islower()` 	- sprawdza czy wszystkie litery są małe

`s.isupper()` 	- sprawdza czy wszystkie litery są duże

`sub in s`        - sprwadza czy napis s zawiera napis sub

`len(s)`        - zwraca ilość liter
`assert len("Skok") == 4`

`s[index]`      - zwraca literę o podanym indeksie


`s[indeksStart:indeksStop]`


`s[indeksStart::krok]`


`s[:indeksStop]`



Listy (list)
############

`list(s)` 	- konwertuje sekwencję s na listę
`assert list((1,2,3)) == [1, 2, 3]`

`l.append(x)` 	- dodaje nowy element x na końcu l, nic nie zwraca!
```python
l = [1]
l.append(2)
assert l == [1, 2]
```

`l.extend(t)` 	- dodaje nową listę t na końcu l, nic nie zwraca!

`l.count(x)` 	- zlicza ilość wystąpień x w l

`l.index(x)` 	- zwraca najmniejszy indeks i, gdzie l[i] == x

`l.pop(i)` 	- zwraca element o indeksie i jednocześnie usuwając go z listy

`l.remove(x)` 	- usuwa z listy l pierwsze wystąpienie elementu x (jeśli nie znajdzie zwraca błąd), nic nie zwraca!

`l.copy()`       - tworzy kopię - zwraca nową listę. To samo co l[:]. Trudno napisać na to ciekawy test :)
`assert [1, 2, 3].copy() == [1, 2, 3]`

`l.reverse()` 	- odwraca kolejność elementów l "w miejscu" (czyli modyfikuje listę), nic nie zwraca!
`l = [2, 1, 3, 0]`

`l.sort()` 	- sortuje elementy l "w miejscu" (czyli modyfikuje listę) - elementy muszą dać się porównywać (np. int i float), nic nie zwraca!

`del l[i]`   - usuwa element o indeksie i z listy, nic nie zwraca!
```python
l = [1, 2, 3]
del l[1]
assert l == [1, 3]
```

`x in l`     - sprawdza czy x jest elementem listy

`len(l)`        - zwraca ilość elementów


