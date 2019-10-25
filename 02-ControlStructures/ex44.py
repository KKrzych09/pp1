speed_limit = int(input("Podaj limit predkosci (km/h): "))
predkosc = int(input("Podaj predkosc pojazdu (km/h): "))

if predkosc <= speed_limit:
    print("Przepisowa jazda, gratulacje :)")
elif predkosc <= speed_limit + 10:
    mandat = (predkosc - speed_limit) * 5
    print(f"Mandat (zł): {mandat}")
elif predkosc > speed_limit:
    mandat = ((predkosc - 10) - speed_limit) * 15 + 50
    print(f"Mandat (zł): {mandat}")