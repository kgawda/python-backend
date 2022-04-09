#!/usr/bin/env python3


def main():
    # 1.
    assert len("konstantynopolitańczykowianeczka") == 32 # długość napisu

    # 2.
    assert "KtO To tAK napISaŁ?!".lower() == 'kto to tak napisał?!'

    # 3.
    assert "1QAZ"[::-1] == "ZAQ1"

    # 4.
    assert "uwaga:sZAzGAyDKfOWr"[6::3] == "szyfr"

    # 5.
    assert "Ala ma kota i psa".split()[2] == "kota" # trzecie słowo

    # 6.
    assert "1,25; 3,14; 22,85".replace(',','.').replace(';', ',') == "1.25, 3.14, 22.85"

    # 7.
    assert ("pies" in "kotek, piesek, chomiczek") == True	  # True czy False?

    # 8.
    assert ("pies" in ["kotek", "piesek", "chomiczek"]) == False # True czy False?

    # 9.
    locations = ["Warszawa"]
    locations.append("Bombaj")
    assert locations == ["Warszawa", "Bombaj"]
    locations.append([48.86, 2.35])
    assert locations == ["Warszawa", "Bombaj", [48.86, 2.35]]
    locations[1] = "Mumbaj"
    assert locations == ["Warszawa", "Mumbaj", [48.86, 2.35]]
    assert locations.pop() == [48.86, 2.35]
    assert locations == ["Warszawa", "Mumbaj"]

    # 10.
    a = [2, 1, 4, 3]
    assert a.sort() == None
    assert a == [1, 2, 3, 4]
    
    print("Wszystko OK!")


if __name__ == "__main__":
    main()

