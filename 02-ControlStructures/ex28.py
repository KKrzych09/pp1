a = 4
b = 15
for i in range(0,a):
    if i == 0:
        for k in range(0,b-1):
            print("*", end = "")
    elif i == a-1:
        for k in range(0,b-1):
            print("*", end = "")
    else:
        print("*", end = "")
        for k in range(0,b-2):
            print(" ", end = "")
    print("*")
