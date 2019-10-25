pesel = str(input("Podaj numer PESEL: "))

if len(pesel) == 11:
    if int(pesel[int(9)]) % 2 != 0:
        print("Płeć: Mężczyzna")
    elif int(pesel[int(9)]) % 2 == 0:
        print("Płeć: Kobieta")
else:
    print("PESEL musi mieć 11 cyfr!")
wiek = 2018 - int(pesel[0:2]) - 1900
print(f'Wiek: {wiek}')