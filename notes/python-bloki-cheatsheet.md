# 🧱 Python – Cheat Sheet: Bloki kodu i dwukropki

W Pythonie nie używa się nawiasów `{}` ani `begin...end`. Zamiast tego stosuje się:

✅ **dwukropek `:`** – otwiera blok kodu  
✅ **wcięcia (indentacja)** – określają, co należy do danego bloku

---

## ✅ Przykłady podstawowych konstrukcji:

### 🔸 `if / elif / else`
```python
a = 5

if a > 0:
    print("Liczba dodatnia")
elif a == 0:
    print("Zero")
else:
    print("Liczba ujemna")

print("To już poza warunkiem")
```

---

### 🔸 `while`
```python
while True:
    print("W pętli")
    if input("Wyjść? ") == "tak":
        break

print("Po pętli")
```

---

### 🔸 `for`
```python
for i in range(3):
    print("Iteracja:", i)

print("Po pętli for")
```

---

### 🔸 `def` – funkcje
```python
def przywitaj(imie):
    print(f"Cześć, {imie}!")

przywitaj("Ania")
```

---

### 🔸 `class` – klasy
```python
class Osoba:
    def __init__(self, imie):
        self.imie = imie

    def przywitaj(self):
        print(f"Cześć, jestem {self.imie}")

o = Osoba("Tomek")
o.przywitaj()
```

---

## ❗ Zasady:

- **Dwukropek `:`** otwiera blok
- **Wcięcie (np. 4 spacje)** = kod należy do bloku
- **Brak wcięcia = koniec bloku**
- Błąd w wcięciu = `IndentationError`

---

💡 Wcięcia są obowiązkowe – to nie styl, to składnia Pythona!
