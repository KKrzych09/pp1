a = int(input('Podaj podstawe: '))
b = int(input('Podaj wykładnik: '))
def potega(x,n):
    pot = x * pow(x,n-1)
    return pot

print(f'{a} do potegi {b} wynosi: {potega(a,b)}')
    