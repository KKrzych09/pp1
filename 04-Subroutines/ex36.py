tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]

def suma(tablica):
    sumaTablicy = 0
    for i in tablica:
        if isinstance(i, int):
            sumaTablicy += i
        else:
            sumaTablicy += suma(i)
    return sumaTablicy
print('Suma wartości całkowitych tej tablicy wynosi:',suma(tab))