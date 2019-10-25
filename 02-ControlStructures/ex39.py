a = 0
b = 1

for i in range(0,50):
    if i == 0:
        print(0)
    else:
        wczesniejsza_wartosc = a
        a = b
        b = wczesniejsza_wartosc + b
        print(a)
    
    
