def transpozycja(macierz):
    print('Macierz: ')
    for i in range(3):
        print('\n')
        for k in range(3):
            print(macierz[i][k], end=' ')
    print('\n\nMacierz transponowana: ')
    for i in range(3):
        print('\n')
        for k in range(3):
            print(macierz[k][i], end=' ')
        
macierz = [[1, 2, 0],[0, 0, 3],[5, 1, 1]]
transpozycja(macierz)