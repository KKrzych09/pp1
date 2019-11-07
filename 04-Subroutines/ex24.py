months = ['Styczeń','Luty','Marzec','Kwiecień','Maj','Czerwiec','Lipiec','Sierpień','Wrzesień','Październik','Listopad','Grudzień']

def miesiac(n):
    i = 0
    while i < len(months):
        if n == i:
            print(months[i-1])
        i += 1
            
miesiac(7)
miesiac(9)