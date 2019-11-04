def suma(tablica):
    x = 0
    i = 0
    print('Tablica: ', end = '')
    while i < len(tablica):
        x += tablica[i]
        i += 1
        print(f'{tablica[i-1]}', end = ' ')
    print('\n')    
    print(f'Suma wartości: {x}')
tab = [4,3,7,1,3]
suma(tab)