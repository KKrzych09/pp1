x = int(input("Podaj liczbe x: "))
y = int(input("Podaj liczbe y: "))

if x == 0 or y == 0:
    print("Nie mozna dzielić przez zero!")
else:
    z = x / y
    print(f"x podzielone przez y wynosi: {z}")