#Zrób funkcję oblicz_vat(cena, stawka) i zwróć cenę brutto.

def oblicz_vat (cena, stawka):
    return round(cena * (1 + stawka), 2)

try:
    cena_netto = float (input("Podaj cenę netto (np. 1245)"))
    stawka_vat = float (input("Podaj stawkę wat w formie dziesiątnej (np. 0.23 dla 23%)"))
    cena_brutto = oblicz_vat(cena_netto, stawka_vat)
    print (f"Cena brutto: {cena_brutto} zł")
except ValueError:
    print("Błąd: Wprowadź poprawne liczby!")
    