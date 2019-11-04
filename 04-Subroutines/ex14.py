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
            m = 1
            break
        elif liczba != tablica[k]:
            m = 0
        k += 1
    if m == 1:
        print("Liczba znajduje się w tablicy.")
    else:
        print("Liczba nie znajduje się w tablicy.")
wystepuje(digit, tab)
    