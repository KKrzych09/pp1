n = int(input("Wprowadz liczbe N: "))
dzielniki = 0

print("N liczb pierwszych: ", end = "")
for i in range(1,n):
    for k in range(1, i+1):
        if i % k == 0:
            dzielniki += 1
    if dzielniki < 3:
        print(f"{i}", end = " ")
    dzielniki = 0
        
