a = int(input("wprowadz dane: "))

if a > 0 and a%2 != 0:
    print("Liczba {} jest dodatnia i nieparzysta".format(a))
else:
    print("Liczba {} jest albo ujemna albo parzysta".format(a))