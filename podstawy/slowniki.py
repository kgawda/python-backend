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


if __name__ == "__main__":
    main()
