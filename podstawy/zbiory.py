def main():
    s = {"a", "b", "c"}
    # set(["a", "b", "c"])  # to też zadziała
    assert "a" in s
    # s[0] - nie można
    for x in s:
        print(x)

    pusty_zbior = set()

    s2 = {"c", "d", "e"}
    print("cz. wspolna", s & s2)
    print("suma", s | s2)
    print("odejmowanie", s - s2)
    print("cz. rozłączna", s ^ s2)

    frozenset([1, 2, 3])  # niemutowalny

    s.add("e")

    print(set("Ala ma kota"))


if __name__ == "__main__":
    main()