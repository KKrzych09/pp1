k = 0
for i in range(0,9):
    if i >= 5:
        for k in range(0,k):
            print("*", end = "")
    else:
        for k in range(0,i):
            print("*", end = "")
    print("*")
    