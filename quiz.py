quiz_pytania = [
    {
        "pytanie": "Jaka jest stolica Polski?",
        "opcje":["A: Kraków","B: Warszawa","C: Gdańsk","D: Bydgoszcz"],
        "odpowiedź": "B"
    },
    {
        "pytanie": "Gdzie jest Wawel?",
        "opcje":["A: Kraków","B: Warszawa","C: Gdańsk","D: Bydgoszcz"],
        "odpowiedź": "A"
    },
    {
        "pytanie": "Gdzie leży Gdańsk",
        "opcje":["A: Nad morzem","B: W centrum Polski","C: W górach","D: Na zachodzie"],
        "odpowiedź": "A"
    },
    {
        "pytanie": "Gdzie leży Warszawa?",
        "opcje":["A: Nad morzem","B: W centrum Polski","C: W górach","D: Na zachodzie"],
        "odpowiedź": "B"
    },
]


def run_quiz(quiz):
    punkty = 0
    for pytanie in quiz:
        print(pytanie["pytanie"])
        for opcja in pytanie['opcje']:
            print(opcja)
        odpowiedź = input("Podaj odpowiedź: ").upper()
        if odpowiedź == pytanie["odpowiedź"]:
            print("Prawidłowa odpowiedź")
            punkty += 1
        else:
            print("Zła odpowiedź")
    print(f"Zdobyłeś {punkty} punktów z zestawu {len(quiz)} pytań")
run_quiz(quiz_pytania)
