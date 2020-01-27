class Stos():
    
    def __init__(self):
        self.karty = []
        
    def wstaw(self, karta):
        self.karty.append(karta)
            
    def zdejmij(self):
        ostatnia_karta = len(self.karty)
        print(f"Zdejmuje karte {self.karty[ostatnia_karta - 1]}")
        self.karty.pop()
        
    def jest_pusty(self):
        if len(self.karty) == 0:
            return "Stos jest pusty"
        else:
            return self.karty

stosik = Stos()

stosik.wstaw(9)
stosik.wstaw(5)
stosik.wstaw(3)
stosik.wstaw("dama")
stosik.wstaw("król")

print(stosik.jest_pusty())

stosik.zdejmij()
print(stosik.jest_pusty())
stosik.zdejmij()
print(stosik.jest_pusty())
