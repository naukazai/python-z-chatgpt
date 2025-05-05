# 📦 requirements.txt Cheat Sheet – zarządzanie zależnościami Pythona

Plik `requirements.txt` służy do określania listy bibliotek potrzebnych do uruchomienia projektu.

---

## ✅ 1. Jak utworzyć `requirements.txt`

Po zainstalowaniu bibliotek w aktywnym środowisku wirtualnym:
```
pip freeze > requirements.txt
```

To zapisze aktualne wersje wszystkich zainstalowanych pakietów.

---

## ✅ 2. Jak zainstalować wszystko z `requirements.txt`

Na nowym komputerze lub w nowym środowisku:
```
pip install -r requirements.txt
```

To automatycznie zainstaluje wszystkie pakiety z listy.

---

## ✅ 3. Jak wygląda przykładowy plik?

```
flask==2.3.2
pandas==2.1.3
openai==1.3.6
```

---

## 🧠 Wskazówki:

- Używaj `freeze` tylko w aktywnym `.venv`
- Wersje (`==`) gwarantują powtarzalność środowiska
- Możesz edytować plik ręcznie, jeśli znasz pakiety

---

💡 Dobrze utrzymany `requirements.txt` = projekt łatwy do uruchomienia gdziekolwiek.
