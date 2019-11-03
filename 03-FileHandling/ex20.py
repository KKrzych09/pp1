tab = []
i = 0
with open('numbers.txt') as file:
    with open('EvenNumbers.txt', 'w') as file2:
        for line in file:
            if int(line) % 2 == 0:
                tab = line
                file2.write(tab)


    