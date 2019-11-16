tablica = [2,3,5,2,9,8,1,3,9,1,1,4,7,7,1,4]

def mediana(tab):
    tab.sort()
    if len(tab) %2 != 0:
        print('Mediana wynosi: ',tab[int(len(tab)/2)])
    else:
        med_parz = (tab[int(len(tab)/2)] + tab[int((len(tab)/2)-1)]) / 2
        print('Mediana wynosi:', med_parz)
def dominanta(tab):
    value = tab[0]
    i = 0
    licznik = 0
    while i < len(tab):
        ileLiczb = tab.count(tab[i])
        if ileLiczb > licznik:
            licznik = ileLiczb
            value = tab[i]
        i += 1
    print('Dominanta: ',value) 
        
    
mediana(tablica)
dominanta(tablica)