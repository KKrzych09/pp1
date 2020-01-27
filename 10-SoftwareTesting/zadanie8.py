class Sala():
    
    def __init__(self, nazwa_sali, liczba_miejsc):
        self.nazwa_sali = nazwa_sali
        self.liczba_miejsc = liczba_miejsc
        
class Sale(Sala):
    
    def __init__(self):
        self.sale = []
   
    def dodaj(self, Sala):
        self.sale.append(Sala)
       
    def liczba_sal(self):
        return f"Liczba sal: {len(self.sale)}"
    
    def razem_miejsc(self):
        suma = 0
        for i in self.sale:
            suma += i.liczba_miejsc
        return f"Miejsca: {suma}"
    
    def liczba_miejsc(self, nazwa_sali):
        for i in self.sale:
            if nazwa_sali == i.nazwa_sali:
                return f"{i.nazwa_sali} ma {i.liczba_miejsc} miejsc"
        return f"Nie ma takiej sali jak {nazwa_sali}"
    
    def liczba_sal_przedzial(self, od, do):
        wybrane_sale = []
        for i in self.sale:
            if i.liczba_miejsc >= od and i.liczba_miejsc <= do:
                wybrane_sale.append(i.nazwa_sali)
        if len(wybrane_sale) > 0:
            return f"Liczba sal z podanego przedziału wynosi {len(wybrane_sale)}"
        
        else:
            return f"Nie ma sali z takim przedziałem ilości miejsc"
        
   
UEK = Sale()
sala1 = Sala("Nowa Aula", 80)
sala2 = Sala("Hala Sportowa", 500)
sala3 = Sala("Lab. komputerowe 115", 35)
sala4 = Sala("Sala 053", 45)
sala5 = Sala("Sala G", 70)

UEK.dodaj(sala1)
print(UEK.liczba_sal())
print(UEK.razem_miejsc())

UEK.dodaj(sala2)
UEK.dodaj(sala3)
UEK.dodaj(sala4)
UEK.dodaj(sala5)

print(UEK.liczba_sal())
print(UEK.razem_miejsc())

print(UEK.liczba_miejsc("Sala 053"))

print(UEK.liczba_sal_przedzial(45, 501))


