tab = []
i = 0
k = 0
with open('universities.txt') as file:
    for line in file:
        tab.append(line)
tab.sort()
for i in tab:
    print(i)
with open('universities.txt', 'w') as file2:
    for k in tab:
        file2.write(k)
    
        