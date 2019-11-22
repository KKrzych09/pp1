import math
# odczytaj współczynniki z klawiatury, zwraca tablicę współczynników
def czytajWspolczynniki():
    wspolczynnik_name = ['a', 'b', 'c']
    wspolczynniki = []
    for i in range(3):
        czytaj = float(input("Podaj współczynnik {}: ".format(wspolczynnik_name[i])))
        wspolczynniki.append(czytaj)
        if wspolczynniki[0] < 0:
            print("Współczynnik 'a' nie może być mniejszy od 0!")
            break
    return wspolczynniki


# oblicz deltę
def obliczDelte(tab: list):
    if tab[0] < 0:
        pass
    else:
        return pow(tab[1], 2) - (4 * tab[0] * tab[2])


# wyznacz pierwiastki równania - zwraca tablicę pierwiastków (jeden lub dwa elementy) lub pustą tablicę, jeśli delta < 0
def obliczPierwiastki(tab: list, discrimant):
    pierwiastki = []
    if discrimant == 0:
        x1 = -tab[1] / 2 * tab[0]
        pierwiastki.append(x1)
        return pierwiastki
    else:
        x1 = (-tab[1] - math.sqrt(discrimant)) / (2 * tab[0])
        x2 = (-tab[1] + math.sqrt(discrimant)) / (2 * tab[0])
        pierwiastki.append(x1)
        pierwiastki.append(x2)
        return pierwiastki
   
   
# wyświetl wyznaczone pierwiastki równania kwadratowego
def wyswietlPierwiastki(tab: list, pierwiastki: list):
    if tab[1] > 0 and tab[2] > 0:
        print(f"Równanie kwadratowe postaci: {tab[0]}x^2+{tab[1]}x+{tab[2]}")
    elif tab[1] > 0 and tab[2] < 0:
        print(f"Równanie kwadratowe postaci: {tab[0]}x^2+{tab[1]}x-{abs(tab[2])}")
    elif tab[1] < 0 and tab[2] > 0:
        print(f"Równanie kwadratowe postaci: {tab[0]}x^2-{abs(tab[1])}x+{tab[2]}")
    elif tab[1] < 0 and tab[2] < 0:
        print(f"Równanie kwadratowe postaci: {tab[0]}x^2-{abs(tab[1])}x-{abs(tab[2])}")
