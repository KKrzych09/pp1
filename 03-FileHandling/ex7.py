suma = 0
with open('C:/Users/s-115-29/Desktop/pp1/03-FileHandling/numbers.txt','r') as file:
    for line in file:
        suma = int(line)
        print(f'{suma}')