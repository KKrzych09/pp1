liczby = ["zero","jeden","dwa","trzy","cztery","pięć","sześć","siedem","osiem","dziewięć"]

numer = str(input("Podaj liczbe: "))

for i in numer:
    print(liczby[int(i)], end = " ")
