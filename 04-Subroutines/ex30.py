import random
def randomowaLiczba(n = 1000):
    i = 0
    parz = 0
    nieparz = 0
    while i <= n:
        x = random.randint(1,50)
        if x % 2 == 0:
            parz += 1
        elif x % 2 != 0:
            nieparz += 1
        i += 1
    print('Liczby parzyste: {}%'.format(parz/n*100))
    print('Liczby nieparzyste: {}%'.format(nieparz/n*100))
print('Dla 1000 liczb losowych z przedziału <1,50>: ')
randomowaLiczba()