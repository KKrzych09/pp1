tab = [15,38,7,23,14]
digit = int(input('Podaj liczbe: '))

def wystepuje(liczba,tablica):
    i = 0
    k = 0
    print('Tablica: ', end = '')
    while i < len(tablica):
        print(tablica[i], end = ' ')
        i += 1
        
    print('\nRezultat: ', end = '')
    while k < len(tablica):
        if liczba == tablica[k]:
            print('Podana liczba wystepuje w tablicy')
            break
        elif liczba != tablica[k]:
            print('Podana liczba nie wystepuje w tablicy')
        k += 1
wystepuje(digit, tab)
    