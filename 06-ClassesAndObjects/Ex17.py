class common_fraction():
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
    
    def display(self):
        print(f"{self.licznik}/{self.mianownik}")
    
    def simplify(self):
        if self.mianownik % self.licznik == 0:
            self.mianownik = int(self.mianownik / self.licznik)
            self.licznik = 1
            print(f"Ułamek po skróceniu wynosi: {self.licznik}/{self.mianownik}")
            
        
        
fraction = common_fraction(1,2)
fraction.display()

fraction2 = common_fraction(12,24)
fraction2.display()
fraction2.simplify()

fraction3 = common_fraction(7,49)
fraction3.display()
fraction3.simplify()
