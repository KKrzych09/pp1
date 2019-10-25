suma = 0
licz = 0
for i in range(100):
    cyfra = int(input("Wprowadz liczbe(0 kończy wprowadzanie): "))
    if cyfra == 0:
        break
    else:
        licz += 1
        suma = suma + cyfra
        srednia = suma / licz
print(f"Rezultat: Ilosc liczb: {i}, suma = {suma}, srednia = {srednia}")