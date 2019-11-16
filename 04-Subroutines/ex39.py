def zakres(x,y,n):
    if n < x or n > y:
        print('Liczba nie znajduje sie w przedziale <x,y>')
    else:
        print('Liczba znajduje sie w przedziale <x,y>')
    
x = int(input('Podaj dolny zakres: '))
y = int(input('Podaj górny zakres: '))
n = int(input('Podaj liczbe: '))
zakres(x,y,n)

