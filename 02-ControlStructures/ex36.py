liczba = int(input("Podaj liczbe: "))

if liczba % 7 == 0 and liczba % 2 == 1 and liczba % 3 == 1 and liczba % 4 == 1 and liczba % 5 == 1 and liczba % 6 == 1:
    print("Liczba jest podzielna przez 7 i przy dzieleniu przez 2,3,4,5,6 daje reszte 1")
else:
    print("zła liczba")