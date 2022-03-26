def main():
    ciekawe_typy = {
        int: 123,
        tuple: (1, 2, 3),
        float: 1.235,
        #Decimal  - na później
        list: [
            list.append,
            list.pop,
            list.insert,
            list.reverse,  # - in place / [::-1] - copy
            list.sort,
            list.clear,
            list.copy, # [:],
            {"przydadza się też funkcje": [min, max, sum, len]},
        ],
        str: [
            "przykładowy str",
            f"f-stringi{'!'}",
            str.split,
            str.join,
            # i wiele innych ważnych
        ],
        dict: "patrz podstawy/slowniki.py",
        set: {1, 2, 3},  # .add, &, |, set(), frozenset(...)
        bool: True,
        None: None,
    }

if __name__ == '__main__':
    main()
