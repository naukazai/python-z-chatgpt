while True:
    dzialanie = input("Wybierz działanie (+,-,*,/,%, koniec): ")

    if dzialanie == "koniec":
        print("Zamykanie kalkulatora. Do zobaczenia!")
        break

    if dzialanie not in ["+", "-", "*", "/", "%"]:
        print("Nieznane działanie!")
        continue

    try:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
    except ValueError:
        print("Błąd: Wprowadź poprawne liczby!")
        continue

    if dzialanie == "+":
        print("Wynik:", round(a + b, 2))
    elif dzialanie == "-":
        print("Wynik:", round(a - b, 2))
    elif dzialanie == "*":
        print("Wynik:", round(a * b, 2))
    elif dzialanie == "/":
        if b == 0:
            print("Nie dziel przez zero!")
        else:
            print("Wynik:", round(a / b, 2))
    elif dzialanie == "%":
        print("Reszta z dzielenia:", a % b)

