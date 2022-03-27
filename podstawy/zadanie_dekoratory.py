import time

def main():
    #1. dekorator liczący czas
    # w środku rozwiązania znajdzie się:

    time_start = time.perf_counter()
    # wywołanie funkcji
    time_end = time.perf_counter()
    print("Wywołanie funkcji zajęło", time_end - time_start)

    #2. dekorator zbierający w listę

    class ListaObiektow:
        def __init__(self):
            self.lista = []

        def dodaj_do_listy(self, x):
            """ Dekorator, możliwy do użycia na obiekcie i funkcji.
            Nie modyfikuje obiektu/funkcji, a jedynie dodaje go do self.lista"""
            pass # TODO

    widoki = ListaObiektow()

    @widoki.dodaj_do_listy
    def home(request):
        return "Witaj na stronie"

    @widoki.dodaj_do_listy
    def greet(request):
        return "Witaj, twój request to " + str(request)

    assert home in widoki.lista
    assert greet in widoki.lista
    assert home(None) == "Witaj na stronie"
    assert greet(1) == "Witaj, twój request to 1"

    # 3. fabryka fukncji-kluczy do sortowania

    l = ["Ala", "pies", "kot", "i tak dalej", "..."]
    l.sort(key=len)  # to by posortowało po długości
    l.sort(key=lambda x: x[1])  # to by posortowało po drugiej literze

    def fabryka_funkcji_pobierajacych_dana_litere(idx_litery):
        pass # TODO
        # zadanie dodatkowe: jeśli jest za mało liter to podać ostatnią

    l.sort(key=fabryka_funkcji_pobierajacych_dana_litere(0))  # ma sortowac po pierszej literze
    l.sort(key=fabryka_funkcji_pobierajacych_dana_litere(1))  # ma sortowac po pierszej literze

    assert fabryka_funkcji_pobierajacych_dana_litere(0)("Abcd") == "A"
    assert fabryka_funkcji_pobierajacych_dana_litere(2)("Abcd") == "c"

if __name__ == '__main__':
    main()