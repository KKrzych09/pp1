import math
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

delta = (b ** 2) - 4 * (a * c)

pierwiastek1 = float(-b - math.sqrt(delta)) / (2 * a)
pierwiastek2 = float(-b + math.sqrt(delta)) / (2 * a)

print(f"Pierwiastek nr 1 wynosi: {pierwiastek1}")
print(f"Pierwiastek nr 2 wynosi: {pierwiastek2}")