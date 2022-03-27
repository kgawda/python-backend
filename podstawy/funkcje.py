import random
import time

def main():
    def f1(arg1, arg2, arg3=333):
        print(arg1, arg2, arg3)
    f1(1, 2, 3)
    f1(1, 2)
    f1(1, arg3=3, arg2=2)
    # nie zadziała: f1(1, arg3=3, 2)
    f1(arg1=1, arg3=3, arg2=2)
    # nie zadziała: f1(arg1=1, 3, 2)

    def f2(*args, **kwargs):
        print(args, kwargs)

    f2(1, 2, 3, test4=4, test5=5, cokolwiek=True)
    f2()

    def f3(arg1, *args, name, **kwargs):
        print(args, kwargs)
    f3(1, 2, 3, name="Test", cokolwiek=1234)

    t = (1, 2, 3)
    f1(*t)  # <--> f1(1, 2, 3)
    d = {'arg1': 1, 'arg2': 2, 'arg3': 3}
    f1(**d)  # <--> f1(arg1=1, arg2=2, arg3=3)

    # przekaż wszystkie argumenty:
    #def f4(*args, **kwargs):
    #    f3(*args, **kwargs)

def funkcja_jako_obiekt():
    def f(x):
        return x
    print(f, type(f))
    identycznosc = f
    assert identycznosc(123) == 123

    kwadrat = lambda x: x ** 2

    #def kwadrat(x):
    #    return x ** 2

    funkcja = random.choice([identycznosc, hex, bin, abs, kwadrat])
    print(funkcja, funkcja.__name__, funkcja(-123))

    ### callback
    def wyslij_mailing(tresc, odbiorcy, done_callback=None):
        """
        Funkcja wysyłająca maile.
        done_callback to funkcja przyjmująca jako argument listę adresatów do których udało się wysłać maila.
        """
        time.sleep(1)
        success = random.randint(0, 100) > 10
        if success:
            if done_callback:
                done_callback(odbiorcy)

    def success_callback(odbiorcy):
        print("Udało się wysłać maile do odbiorców: " + ", ".join(odbiorcy))

    print(wyslij_mailing.__doc__)
    wyslij_mailing("Witaj!", ["a@b.pl", "c@d.pl"], success_callback)

    wyslij_mailing("Witaj!", ["a@b.pl", "c@d.pl"], lambda lista: print(f"Wysłano do {lista}"))

    def fabryka_funkcji_potegujacych(n):
        def potega(x):
            return x ** n
        return potega

    szescian = fabryka_funkcji_potegujacych(3)
    print(szescian(32))

    ### ZADANIE ###
    def dodaj_wydruki(f):
        def wrapper(*args, **kwargs):
            print("Start funkcji")
            result = f(*args, **kwargs)
            print("Koniec funkcji")
            return result
        return wrapper

    def kwadrat(x):
        print("Liczę kwadrat z", x)
        return x ** 2

    kwadrat_z_wydrukami = dodaj_wydruki(kwadrat)
    rezultat = kwadrat_z_wydrukami(2)
    # wydruk: Start funkcji
    # wydruk: Koniec funkcji
    assert rezultat == 4

    @dodaj_wydruki
    def szscian(x):
        print("Liczę szscian z", x)
        return x ** 3

    # @dodaj_wydruki przed definicją funkcji znaczy to samo co po definicji zrobienie:
    # szescian = dodaj_wydruki(szescian)

    result = szscian(234)
    print(result)

if __name__ == '__main__':
    main()
    funkcja_jako_obiekt()