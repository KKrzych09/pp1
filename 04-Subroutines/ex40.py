tablica = [1,2,3,4,5,6,7,8]
parz = lambda a: a % 2 == 0

x = filter(parz,tablica)

for i in x:
    print(i)