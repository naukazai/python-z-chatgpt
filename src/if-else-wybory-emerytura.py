x = int(input("Ile masz lat: "))
# Głosowanie
if x >= 18:
    print("Jesteś pełnoletni - możesz głosować")
else:
    print("Jesteś niepełnoletni - nie możesz głosować")
# Emerytura
if x >= 65:
    print("Możesz iść na emeryturę")
else:
    print("Nie możesz isć na emeryturę")