x = int(input('Podaj liczbe(dla wartosci 500 wprowadz 0): '))
if x == 0:
    x = 500
def suma(N):
    suma = 0
    for i in range(1,N+1):
        suma += i
    print(suma)
    
print('Suma liczb: ', end = '')
suma(x)