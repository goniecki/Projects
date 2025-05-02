import random

slowa = ["python","ruby","swift","java","javascript","cpp"]

wybrane_slowo = random.choice(slowa) # losowy wybrór słowa
wyswietlane_slowo = ["_" for _ in wybrane_slowo] # tworzy listę podkreślników
proby = 8  # ilość prób

print("Witam w wisielcu (hangman)")

while proby > 0 and "_" in wyswietlane_slowo:
    print ("\n" + " ".join(wyswietlane_slowo))
    podana_litera = input("Podaj literę: ").lower()
    if podana_litera in wybrane_slowo:
        for index, letter in enumerate(wybrane_slowo):
            if letter == podana_litera:
                wyswietlane_slowo[index] = podana_litera
    else:
        print('Nie ma takiej litery')
        proby -= 1
        print("Pozostała liczba prób",proby)
if "_" not in wyswietlane_slowo:
    print("Brawo zgadłeś słowo!")
    print("".join(wyswietlane_slowo))
else:
    print("Nie ma już więcej prób, nie udało się.")
