# 🧠 Git Cheat Sheet – Python z ChatGPT

Ten plik zawiera podstawowy zestaw komend Git do codziennej pracy z repozytorium.

---

## ✅ Jak wypchnąć nowy plik lub zmiany do GitHuba

1️⃣ Sprawdź, co się zmieniło:
```
git status
```

2️⃣ Dodaj konkretny plik:
```
git add src/nazwapliku.py
```

...lub dodaj wszystko:
```
git add .
```

3️⃣ Zatwierdź zmiany z opisem:
```
git commit -m "Dodano nazwapliku.py – krótki opis zmian"
```

4️⃣ Wypchnij zmiany na GitHub:
```
git push origin main
```

---

## 📝 Przykład:

Dodałeś plik `gra.py`:
```
git add src/gra.py
git commit -m "Dodano gra.py – mini gra tekstowa"
git push origin main
```

---

## 💡 Pro tip:

Jeśli często robisz to samo, możesz utworzyć alias:
```
git config --global alias.acp "!git add . && git commit -m"
```

Potem używasz:
```
git acp "Opis zmian"
git push
```
