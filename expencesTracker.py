import json

def dodaj_wydatek(wydatki, opis_wydatku, wartosc_wydatku):
    wydatki.append({"opis wydatku": opis_wydatku, "wartosc wydatku": wartosc_wydatku})
    print(f"Dodany wydatek: {opis_wydatku}, Wartosc wydatku: {wartosc_wydatku}" )

def podaj_wydatki(wydatki):
    sum = 0
    for wydatek in wydatki:
        sum += wydatek["wartosc wydatku"]
    return sum

def pozostaly_budzet(budzet, wydatki):
    return budzet - podaj_wydatki(wydatki)

def podaj_szczegoly_budzetu(budzet, wydatki):
    print(f"Budżet: {budzet}")
    print("Wydatki: ")
    for wydatek in wydatki:
        print(f"- {wydatek['opis wydatku']}: {wydatek['wartosc wydatku']}")
    print(f"Wszystkie wydatki:  {podaj_wydatki(wydatki)}")
    print(f"Pozostały budżet: {pozostaly_budzet(budzet, wydatki)}")

def zaladuj_budzet_data(sciezka_pliku):
    try:
        with open(sciezka_pliku,"r") as file:
            data = json.load(file)
            return data["budzet poczatkowy"], data["wydatki"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []

def zapisz_szczegoly_budzetu(sciezka_pliku,poczatkowy_budzet,wydatki):
    data = {
        "budzet poczatkowy": poczatkowy_budzet,
        "wydatki": wydatki
    }
    with open(sciezka_pliku,"w") as file:
        json.dump(data,file,indent =4)

def main():
    print("Witam w monitorze wydatków")
    sciezka_pliku = "budzet_data.json"
    poczatkowy_budzet, wydatki = zaladuj_budzet_data(sciezka_pliku)
    if poczatkowy_budzet == 0:
        poczatkowy_budzet = float(input("Wprowadź budżet początkowy: "))
    budzet = poczatkowy_budzet

    while True:
        print("\nCo byś chciał zrobić?")
        print("1. Dodaj wydatek")
        print("2. Pokaż szczegóły budżetu")
        print("3. Wyjdź z programu")
        wybor = input("Wybież działanie (1/2/3): ")

        if wybor == "1":
            opis_wydatku = input("Wpisz opis wydatku: ")
            wartość_wydatku = float(input("Podaj wartość wydatku: "))
            dodaj_wydatek(wydatki, opis_wydatku, wartość_wydatku)
        elif wybor == "2":
            podaj_szczegoly_budzetu(budzet, wydatki)
        elif wybor == "3":
            zapisz_szczegoly_budzetu(sciezka_pliku,poczatkowy_budzet,wydatki)
            print("Wyjście z programu")
            break
if __name__ == '__main__':
    main()

def zaladuj_budzet_data(sciezka_pliku):
    try:
        with open(sciezka_pliku,"r") as file:
            data = json.load(file)
            return data["budzet poczatkowy"], data["wydatki"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []

def zapisz_szczegoly_budzetu(sciezka_pliku,poczatkowy_budzet,wydatki):
    data = {
        "budzet poczatkowy": poczatkowy_budzet,
        "wydatki": wydatki
    }
    with open(sciezka_pliku,"w") as file:
        json.dump(data,file,indent =4)

def main():
    print("Witam w monitorze wydatków")
    sciezka_pliku = "budzet_data.json"
    poczatkowy_budzet, wydatki = zaladuj_budzet_data(sciezka_pliku)
    if poczatkowy_budzet == 0:
        poczatkowy_budzet = float(input("Wprowadź budżet początkowy: "))
    budzet = poczatkowy_budzet

    while True:
        print("\nCo byś chciał zrobić?")
        print("1. Dodaj wydatek")
        print("2. Pokaż szczegóły budżetu")
        print("3. Wyjdź z programu")
        wybor = input("Wybież działanie (1/2/3): ")

        if wybor == "1":
            opis_wydatku = input("Wpisz opis wydatku: ")
            wartość_wydatku = float(input("Podaj wartość wydatku: "))
            dodaj_wydatek(wydatki, opis_wydatku, wartość_wydatku)
        elif wybor == "2":
            podaj_szczegoly_budzetu(budzet, wydatki)
        elif wybor == "3":
            zapisz_szczegoly_budzetu(sciezka_pliku,poczatkowy_budzet,wydatki)
            print("Wyjście z programu")
            break
if __name__ == '__main__':
    main()
