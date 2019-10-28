x = 1
with open('C:/Users/s-115-29/Desktop/pp1/03-FileHandling/NoEducation.txt','r') as file:
    for line in file:
        print(f'{x}. {line}', end = '')
        x += 1