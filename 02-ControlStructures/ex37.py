x = int(input("Podaj pierwsza liczbe: "))
y = int(input("Podaj druga liczbe: "))
z = int(input("Podaj trzecia liczbe: "))

if x > y and x < z or x < y and x > z:
    mediana = x
elif y > x and y < z or y < x and y > z:
    mediana = y
else:
    mediana = z
print(f"Madiana wynosi: {mediana}")