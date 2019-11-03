import re
suma = 0
with open('land.txt', 'r') as file:
    numer = re.findall('\d',file.read())
    for i in numer:
        suma += int(i)
    print(suma)