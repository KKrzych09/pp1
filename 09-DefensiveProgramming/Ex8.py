from math import sqrt

try:
    number = int(input("Wprowadz liczbe: "))
    root = sqrt(number)
    print("Pierwiastek kwadratowy {} wynosi: {}".format(number, root))
except:
    print("Wprowadz liczbe wieksza od 0")