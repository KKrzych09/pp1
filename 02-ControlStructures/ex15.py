x = int(input("Wprowadz liczbe ktora ma byc mnozona: "))

#trzeci parametr w range określałby co ile pętla ma sie wykonywać(np co 2)
for i in range(1,11): 
    a = x * i
    print("{} * {} = {}".format(x,i,a))