ocena = int(input("Podaj ocene w postaci liczby: "))

slowo = ['niedostateczny', 'dopuszczajacy', 'dostateczny', 'dobry', 'bardzo dobry', 'celujacy']

if ocena < 1:
    print("Ocena nie moze byc ujemna!")
elif ocena == 1:
    print(f"Ocena słownie: {slowo[0]}")
elif ocena == 2:
    print(f"Ocena słownie: {slowo[1]}")
elif ocena == 3:
    print(f"Ocena słownie: {slowo[2]}")
elif ocena == 4:
    print(f"Ocena słownie: {slowo[3]}")
elif ocena == 5:
    print(f"Ocena słownie: {slowo[4]}")
elif ocena == 6:
    print(f"Ocena słownie: {slowo[5]}")
elif ocena > 6:
    print("Ocena nie moze byc wyższa niz 6!")