import random
class plane():
    def __init__(self, numer_lotu):
        self.numer_lotu = numer_lotu
        self.wysokosc = 0
    
    def status(self):
        print(f"Tu {self.numer_lotu}, moja wysokość lotu to {self.wysokosc}m.")
        
    def start(self):
        self.wysokosc = random.randint(1000,2000)
        print("Samolot wystartował.")
    
    def change_haltitude(self, change_to):
        if change_to < self.wysokosc and self.wysokosc > 500:
            if abs(change_to - self.wysokosc) < 300 or abs(change_to - self.wysokosc) > 11000:
                print(f"Nie mozna zmniejszyc wysokości o {abs(change_to - self.wysokosc)}m!")
            else:
                print(f"Zmniejszam wysokość o {abs(change_to - self.wysokosc)}m żeby osiągnąć {change_to}m.")
                self.wysokosc = change_to
                
        elif change_to == self.wysokosc:
            print(f"Nie możesz zmienjszyc/zwiekszyc wysokości do {change_to} ponieważ już na niej jesteś.")
            
        else:    
            if change_to - self.wysokosc < 300 or change_to - self.wysokosc > 11000:
                print(f"Nie mozna zwiekszyc wysokości o {change_to - self.wysokosc}m!")
            else:
                print(f"Zwiększam wysokość o {change_to - self.wysokosc}m żeby osiągnąć {change_to}m.")
                self.wysokosc = change_to
    
    def landing(self):
        if self.wysokosc > 500:
            print(f"Zbyt duża wysokość dla lądowania ({self.wysokosc}). Obniż lot")
        else:
            print("Rozpoczynam lądowanie.")
            self.wysokosc = 0


samolot = plane("LOT881")

samolot.status()
samolot.start()
samolot.status()
samolot.change_haltitude(8900)
samolot.status()
samolot.change_haltitude(200)
samolot.status()
samolot.landing()
samolot.status()