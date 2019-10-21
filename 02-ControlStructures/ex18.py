for i in range(1,31):
    if i % 3 == 0 and not i % 5 == 0:
        print("THREE")
    elif i % 5 == 0 and not i % 3 == 0:
        print("FIVE")
    elif i % 3 == 0 and i % 5 == 0:
        print("BINGO")
    else:
        print(f"{i}")