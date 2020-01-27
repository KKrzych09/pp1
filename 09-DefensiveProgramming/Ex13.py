netto = int(input('Podaj cene netto: '))
if netto > 0 and type(netto) == int or type(netto) == float:
    brutto = netto + (netto * 0.23)
    print('Cena brutto wynosi: {:.2f}zl'.format(brutto))