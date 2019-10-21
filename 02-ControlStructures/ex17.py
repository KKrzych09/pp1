n = 0
m = 0
srParz = 0
srNieparz = 0
for i in range(1,51):
    if i % 2 != 0:
       srNieparz += i
       n += 1
    elif i % 2 == 0:
       srParz += i
       m += 1
print(f"Srednia arytmetyczna liczb nieparzystych jest równa: {srNieparz/n}")
print(f"Srednia arytmetyczna liczb nieparzystych jest równa: {srParz/m}")