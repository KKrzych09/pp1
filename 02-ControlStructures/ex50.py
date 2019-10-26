import math
numer = int(input("Podaj liczbę: "))
bin = ""
while numer != 1:
    bin += str(numer % 2)
    numer = int(numer/2)
bin += "1"
print(bin[::-1])