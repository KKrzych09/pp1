tab = [['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]

with open('ex24.csv', 'w') as file:
    file.write('Imie,Nazwisko,Email\n')
    for wiersz in tab:
        file.write(','.join(wiersz))
        file.write('\n')
