dogAge = int(input("Podaj wiek psa w ludzkich latach: "))

wynik = 0

if dogAge <= 2:
    wynik = dogAge * 10.5
    print(f"Wiek psa w psich latach to: {wynik}")
elif dogAge > 2:
    wynik = ((dogAge - 2) * 4) + 21
    print(f"Wiek psa w psich latach to: {wynik}")