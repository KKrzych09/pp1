wiek = 23
if wiek <= 0 or wiek >= 120:
    raise ValueError('Wiek powinien byc z przedzialu <0, 120>')
if type(wiek) != int:
    raise TypeError('Wiek powinien być liczbą całkowitą!')
print(f'Masz {wiek} lat')
