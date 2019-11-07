def jestImie(imie, imiona): 
    print('Imiona: ', end = '')
    for i in imiona:
        print(i, end = ' ')
    print(f'\nImie: {imie}', end = '')
    i = 0
    k = 0
    while i < len(imiona):
        if imiona[i] == imie:
            k = imie
        i += 1
    if imie == k:
        print('\nRezultat: imie zawarte jest w wykazie imion')
    else:
        print('\nRezultat: tego imienia nie ma w wykazie')
    
jestImie('Wojtek',['Janek','Ania','Wojtek','Zosia'])
    