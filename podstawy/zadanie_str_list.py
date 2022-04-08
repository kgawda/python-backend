#!/usr/bin/env python3


def main():
    # 1.
    assert ______("konstantynopolitańczykowianeczka") == 32 # długość napisu

    # 2.
    assert "KtO To tAK napISaŁ?!"___________________ == 'kto to tak napisał?!'

    # 3.
    assert "1QAZ"___________________________________ == "ZAQ1"

    # 4.
    assert "uwaga:sZAzGAyDKfOWr"________________ == "szyfr"

    # 5.
    assert "Ala ma kota i psa"_________________________[2] == "kota" # trzecie słowo

    # 6.
    assert "1,25; 3,14; 22,85"_________________________ == "1.25, 3.14, 22.85"

    # 7.
    assert ("pies" in "kotek, piesek, chomiczek") == _____	  # True czy False?

    # 8.
    assert ("pies" in ["kotek", "piesek", "chomiczek"]) == _____ # True czy False?

    # 9.
    locations = ["Warszawa"]
    locations._________("Bombaj")
    assert locations == ["Warszawa", "Bombaj"]
    locations._________([48.86, 2.35])
    assert locations == ["Warszawa", "Bombaj", [48.86, 2.35]]
    locations[___] ____ "Mumbaj"
    assert locations == ["Warszawa", "Mumbaj", [48.86, 2.35]]
    assert locations._________()  == [48.86, 2.35]
    assert locations == ["Warszawa", "Mumbaj"]

    # 10.
    a = [2, 1, 4, 3]
    assert a.sort() == ____________
    assert a == ________________
    
    print("Wszystko OK!")


if __name__ == "__main__":
    main()

