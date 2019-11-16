tablica = [1,1,2,3,4,5,5,6,6]

def bezPowtorzen(tab):
    return list(dict.fromkeys(tab))

print(bezPowtorzen(tablica))

