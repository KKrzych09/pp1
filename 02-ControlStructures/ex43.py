x = int(input("Podaj pierwszą liczbę: "))
y = int(input("Podaj drugą liczbę: "))
z = int(input("Podaj trzecią liczbę: "))

if x < y < z:
    print(f"Liczby w kolejności rosnącej: {x,y,z}")
elif x < z < y:
    print(f"Liczby w kolejności rosnącej: {x,z,y}")
elif y < x < z:
    print(f"Liczby w kolejności rosnącej: {y,x,z}")
elif y < z < x:
    print(f"Liczby w kolejności rosnącej: {y,z,x}")
elif z < x < y:
    print(f"Liczby w kolejności rosnącej: {z,x,y}")
elif z < y < x:
    print(f"Liczby w kolejności rosnącej: {z,y,x}")
    