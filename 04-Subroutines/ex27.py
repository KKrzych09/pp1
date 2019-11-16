import re
text = 'Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'
def vowels(txt):
    samogloski = 'aeiouy'
    x = txt.casefold #zamienia wielkie litery na male w calym tekscie
    licz = {}.fromkeys(samogloski, 0) #tworzy slownik z podanych liter (samogloski) 
    for litera in txt: 
        if litera in licz: 
            licz[litera] += 1    
    return licz
print(vowels(text))