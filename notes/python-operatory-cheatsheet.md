# 🧠 Python – Operatory: mini ściąga

Przydatne operatory logiczne i porównania w Pythonie – idealne do `if`, `while`, warunków w pętlach i quizach.

---

## ✅ Operatory przypisania vs porównania

| Operator | Znaczenie         | Przykład             |
|----------|------------------|----------------------|
| `=`      | przypisanie       | `x = 10`             |
| `==`     | porównanie        | `x == 10` → `True`   |

---

## 🔍 Operatory porównania

| Operator | Znaczenie               | Przykład        |
|----------|--------------------------|------------------|
| `!=`     | różne                    | `x != 5`        |
| `>`      | większe niż              | `x > 10`        |
| `<`      | mniejsze niż             | `x < 3`         |
| `>=`     | większe lub równe        | `x >= 8`        |
| `<=`     | mniejsze lub równe       | `x <= 100`      |

---

## 🔗 Operatory logiczne

| Operator | Znaczenie           | Przykład                  |
|----------|---------------------|----------------------------|
| `and`    | i (oba warunki)     | `x > 5 and x < 10`        |
| `or`     | lub (jeden z warunków) | `x < 0 or x > 100`     |
| `not`    | zaprzeczenie         | `not x == 10`            |

---

## 📦 Inne przydatne

| Operator | Znaczenie           | Przykład                  |
|----------|---------------------|----------------------------|
| `in`     | czy coś zawiera się | `'a' in 'abc'` → `True`    |
| `is`     | czy to dokładnie ten sam obiekt | `a is b` |

---

## ✅ Przykładowe użycie w kodzie:

```python
x = 7

if x > 5 and x < 10:
    print("x jest w przedziale")

if x != 0:
    print("x nie jest zerem")

if not x == 10:
    print("x to nie 10")
```

---

💡 Używaj `and`, `or`, `not` i operatorów porównań do budowania warunków w `if`, `while`, `elif`, itp.
