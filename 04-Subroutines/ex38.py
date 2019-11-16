import re
def wielkieLitery(txt):
    for i in txt:
        x = re.findall('[A-Z]', txt)
        if i.isupper():
            print(i, end = ' ')

wielkieLitery(str(input('Podaj tekst: ')))