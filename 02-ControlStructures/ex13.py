x = int(input("Wprowadz wspolrzedna x: "))
y = int(input("Wprowadz wspolrzedna y: "))

if x < 0 and y > 0:
    print("Punkt P({},{}) lezy w pierwszej cwiartce".format(x,y))
elif x > 0 and y > 0:
    print("Punkt P({},{}) lezy w drugiej cwiartce".format(x,y))
elif x < 0 and y < 0:
    print("Punkt P({},{}) lezy w trzeciej cwiartce".format(x,y))
else:
    print("Punkt P({},{}) lezy w czwartej cwiartce".format(x,y))