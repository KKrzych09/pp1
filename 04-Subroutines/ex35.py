def sumaCyfr(n):
    if n == 0:
        return 0
    return n % 10 + sumaCyfr(n // 10)

liczba = int(input('Podaj liczbe: '))
print('Suma cyfr tej liczby jest równa:',sumaCyfr(liczba))