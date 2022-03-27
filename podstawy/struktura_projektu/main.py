print("Otwieram plik main")
import random
from random import randrange
from random import randbytes, getrandbits
#from random import *  # zła praktyka
#import random as rd  # niektóre biblioteki mają utartą tradycję żeby tak je importować
#from random import randrange as random_range  # ostrożnie z tym!

import a
import module1.base
import module2.base
from module1 import base

if __name__ == '__main__':
    print(random.randint(1, 100))
    print(randrange(1, 101))
    print(a, type(a))
    a.licznik += 1

    print(a.licznik)
    print(module1.base.licznik)
    print(base.licznik)
    print(module2.base.licznik)
