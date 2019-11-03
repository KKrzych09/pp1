tab = [32, 16, 5, 8, 24, 7]
i = 0
with open('./tablica.txt', 'a') as file:
    while i < len(tab):
        file.write(str(tab[i]))
        file.write('\n')
        i += 1
