tab = []
i = 0
with open('numbers.txt') as file:
    for line in file:
        tab.append(int(line))
tab.sort()
for i in tab:
    print(i, end = ' ')
  