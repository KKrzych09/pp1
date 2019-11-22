import QuadraticEquation 

abc = QuadraticEquation.czytajWspolczynniki()
if abc[0] > 0:
    delta = QuadraticEquation.obliczDelte(abc)
    print("Delta = {}".format(int(delta)))
    if delta < 0:
        print("Delta ujemna, brak pierwiastków.")
    else:
        wynik = QuadraticEquation.obliczPierwiastki(abc,delta)

        abc = [round(x) for x in abc]
        QuadraticEquation.wyswietlPierwiastki(abc,wynik)
    
        if len(wynik) == 1:
            print(f"Pierwiastki równania: x1 = {wynik[0]}")
        else: 
            print(f"Pierwiastki równania: x1 = {wynik[0]}, x2 = {wynik[1]}")
