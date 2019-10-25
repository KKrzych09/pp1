import random
j = 0
d = 0
t = 0
c = 0
p = 0
s = 0
for i in range(0,100):
    x = random.randint(1,6)
    if x == 1:
        j += 1
    elif x == 2:
        d += 1
    elif x == 3:
        t += 1
    elif x == 4:
        c += 1
    elif x == 5:
        p += 1
    elif x == 6:
        s += 1
print(f"Jedynka: {j}")
print(f"Dwójka: {d}")
print(f"Trójka: {t}")
print(f"Czwórka: {c}")
print(f"Piątka: {p}")
print(f"Szóstka: {s}")
        