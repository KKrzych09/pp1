imiona = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy', 'Teofil']

dlugosc = 0
z = 0

for i in range(0,len(imiona)):
    if len(imiona[i]) > len(imiona[i-1]):
        if len(imiona[i]) > dlugosc:
            dlugosc = len(imiona[i])
            z = i
print(f"Najdluzsze imie: {imiona[z]}")