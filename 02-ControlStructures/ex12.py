x = int(input("Wprowadz x: "))
y = int(input("Wprowadz y: "))

if x < 0 and y < 0:
    print("Liczba {} i liczba {} sa ujemne".format(x,y))
elif x > 0 and y < 0:
    print("Liczba {} jest dodatnia a liczba {} jest ujemna".format(x,y))
elif x < 0 and y > 0:
    print("Liczba {} jest ujemna a liczba {} jest dodatnia".format(x,y))
else:
    print("Liczba {} i liczba {} sa dodatnie".format(x,y))