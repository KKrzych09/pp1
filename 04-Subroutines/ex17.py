import random
def rzucKostka():
    suma = 0
    print('Wyrzucone oczka: ', end = '')
    for i in range(3):
        x = random.randint(1,6)
        print(f'{x}', end = ' ')
        suma += x
    print(f'\nSuma oczek: {suma}')
    
rzucKostka()