def main():
    d = {"a": 1, "b": 2, 1: 1, (1, 2): 2}
    #d = dict(a=1, b=2)  # działa ale tylko dla kluczy typu str
    d['c'] = 3
    d.update({1: 111, 2: 222})
    # pop, clear, items, keys, values, get
    print(d, type(d))
    assert d['c'] == d.get('c')
    assert d.get('d', "Nieznany") == "Nieznany"

    if 'c' in d:
        print("pod kluczem 'c' jest", d['c'])
    else:
        print("pod kluczem 'c' nie ma nic")

    #klucze:
    #for x in d:  # ewenutalnie d.keys()
    #    print(x)

    # for key, value in d.items():
    #     print(f"{key}: {value}")

    for n, (key, value) in enumerate(d.items()):
        print(n, key, value)


def klasy_i_slowniki():

    class A:
        pole1 = 1
        def __init__(self):
            self.x = 1
            self.y = 2

    a = A()
    a.x = 111
    a.z = 333  # można dodać w trakcie życia obiektu, ale to nieeleganckie
    print(vars(a))
    # do klasy też mona dopisać:
    print(A.pole1, a.pole1)
    a.pole1 = 111
    print(A.pole1, a.pole1, vars(a))
    A.pole2 = 2
    print(A.pole2, a.pole2)
    a.pole2 = 222
    print(A.pole2, a.pole2, vars(a))

if __name__ == "__main__":
    main()
    klasy_i_slowniki()
