import random

imiona = ["Burek", "Rex", "Reksio", "Diesel"]

def main():
    class AnimalException(Exception):
        pass

    class Zwierzak:
        wolne_imiona = set(imiona)
        def __init__(self, name, **kwargs):
            self.name = name

        def przedstaw_sie(self):
            return f"Jestem {self.name}"

        @classmethod
        def z_losowym_imieniem(cls, race=None):
            if cls.wolne_imiona:
                return cls(cls.wolne_imiona.pop(), race=race)
            else:
                raise AnimalException("Brak wolnych imion")

        @staticmethod
        def wylosuj(collection):
            return random.choice(collection)

    class Pies(Zwierzak):
        glos = "Hau Hau!"

        # def __new__(...)  # tak można obsłużyć klasy dla poszczególnych ras

        def __init__(self, name, race, **kwargs):
            super().__init__(name, **kwargs)
            self.race = race

        def daj_glos(self):
            return self.glos

    # class Husky(Pies):
    #     glos = "Uuuuuu"

    class Kot(Zwierzak):
        glos = "Miau"
        def __init__(self, name, kolor_siersci, **kwargs):
            super().__init__(name,  **kwargs)
            self.kolor_siersci = kolor_siersci

    z = Pies("Fafik", "Buldog")
    print(z.przedstaw_sie())

    try:
        for _ in range(5):
            z2 = Pies.z_losowym_imieniem("York")
            print(z2.przedstaw_sie(), z2.daj_glos())
    except AnimalException as e:
        pass
        # w zmiennej e mamy wyjątek

    print(Pies.wylosuj((1, 2, 3, 4)))

    class PsoKot(Pies, Kot):
        glos = "Hau Miau"
        def __init__(self, name, race, kolor_siersci):
            super().__init__(name, race=race, kolor_siersci=kolor_siersci)

    #print(PsoKot.__mro__)  - wartościowa ściągawka - Method Resolution Order
    pk = PsoKot("Henryk", race="Psokot Andaluzyjski", kolor_siersci="Niebieski")
    print(pk.daj_glos())

def metody_specjalne():
    class A:
        def __init__(self):
            self.counter = 0

        def __str__(self):
            return f"<Obiekt Klasy A, counter={self.counter}>"

        def __getitem__(self, item):
            return f"Wartość pod indeksem {item}"

        def __getattr__(self, item):
            def f():
                print("wywołuję", item)
                self.counter += 1
                return self
            return f

    a = A()
    print(a)
    print(a[123])
    print(a.increased().compared().sorted())

if __name__ == '__main__':
    main()
    metody_specjalne()