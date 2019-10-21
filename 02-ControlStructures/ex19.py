wyrazyCiagu = int(input("Podaj liczbe wyrazow ciagu: "))
x = 1
i = 0
print("Ciag arytmetyczny o roznicy 3: ")

while i < wyrazyCiagu - 1:
    if x == 1:
        print(f"{x}")
    x += 3
    i += 1
    print(f"{x}")