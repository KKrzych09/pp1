tab = []
tab1 = []
i = 0
k = 0
suma = 0
with open('numbersinrows.txt') as file:
    for line in file:
        tab.append(line.split(','))   
    while i < len(tab):
        tab1 += tab[i]
        i += 1
    for k in tab1:
        suma += int(k)
    print(f"W pliku znajduje się {len(tab1)} liczb")
    print(f"Suma tych liczb wynosi {suma}")
        