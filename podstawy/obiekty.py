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

        def __init__(self, name, race):
            super().__init__(name)
            self.race = race

        def daj_glos(self):
            return self.glos

    # class Husky(Pies):
    #     glos = "Uuuuuu"

    z = Pies("Fafik", "Buldog")
    print(z.przedstaw_sie())

    try:
        for _ in range(5):
            z2 = Pies.z_losowym_imieniem()
            print(z2.przedstaw_sie(), z2.daj_glos())
    except AnimalException as e:
        pass
        # w zmiennej e mamy wyjątek

    print(Pies.wylosuj((1, 2, 3, 4)))

if __name__ == '__main__':
    main()