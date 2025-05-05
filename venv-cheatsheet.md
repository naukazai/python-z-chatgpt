# 🧪 Python venv Cheat Sheet – środowiska wirtualne

To krótka ściąga, jak tworzyć, aktywować i używać wirtualnych środowisk (`venv`) w Pythonie.

---

## ✅ 1. Tworzenie środowiska

W katalogu projektu:
```
python -m venv .venv
```

Utworzy folder `.venv` z oddzielną instalacją Pythona.

---

## ✅ 2. Aktywacja środowiska

🔹 **Windows (PowerShell):**
```
.venv\Scripts\Activate.ps1
```

🔹 **Windows (CMD):**
```
.venv\Scripts\activate.bat
```

🔹 **Windows (czasem potrzebne odblokowanie skryptów):**
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

🔹 **Linux / MacOS:**
```
source .venv/bin/activate
```

---

## ✅ 3. Dezaktywacja środowiska

Działa wszędzie:
```
deactivate
```

---

## ✅ 4. Instalowanie paczek do środowiska

Po aktywacji:
```
pip install nazwa_paczki
```

Przykład:
```
pip install flask
```

---

## ✅ 5. Zapisywanie zależności

Po zainstalowaniu pakietów:
```
pip freeze > requirements.txt
```

Aby odtworzyć środowisko na innym komputerze:
```
pip install -r requirements.txt
```

---

💡 Używaj `.venv`, żeby trzymać porządek i nie mieszać globalnych paczek systemowych z projektowymi!
