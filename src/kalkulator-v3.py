a = float (input ("Podaj pierwszą liczbę "))
b = float (input ("Podaj drugą liczbę "))
dzialanie = input("Wybierz działanie (+,-,*,/,%): ")
if dzialanie == "+":
    print("Wynik:", a + b)
elif dzialanie == "-":
    print("Różnica:", a-b)
elif dzialanie == "-":
    print("Iloczyn:", a*b)
elif dzialanie == "-":
    print("Iloraz:", a/b)
elif dzialanie == "-":
    print("Reszta z dzielenia:", a%b)
else: 
    print ("Nieznane działanie!")