n = int(input("Wprowadz liczbe N: "))

print("N liczb pierwszych: ", end = "")
for i in range(1,n+1):
    if i % 1 == 0 and i % i == 0:
        print(f"{i}", end = " ")
        