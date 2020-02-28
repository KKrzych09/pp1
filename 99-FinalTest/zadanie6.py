class Restauracja():
    
    def __init__(self):
        self.stoliki = [1, 2, 3, 4, 5]
    
    def rezerwuj(self, nr_stolika):
        if nr_stolika in self.stoliki:
            self.stoliki.remove(nr_stolika)
  
        elif (nr_stolika not in self.stoliki) and (nr_stolika <= 5 and nr_stolika >= 1):
            print("Stolik jest juz zarezerwowany")
        else:
            print("Nie ma takiego stolika")
        
    def zwolnij(self, nr_stolika):
        if nr_stolika not in self.stoliki:
            if nr_stolika >= 1 and nr_stolika <= 5:
                self.stoliki.append(nr_stolika)
            else:
                print("Nie ma takiego stolika")
        else:
            print("Stolik jest juz zwolniony")
        
    def ile_wolnych(self):          
        result = f"Wolne stoliki to: {sorted(self.stoliki)}"
        return result
        



        