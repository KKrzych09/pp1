import statistics
class statystyka():
    def __init__(self, numbers):
        self.numbers = numbers
        self.lista = []
    
    def display(self):
        self.lista = self.numbers.split(", ")
        self.lista = [int(i) for i in self.lista]
        print("Podane liczby: ", end = '')
        for i in self.lista:
            print(i, end = ' ')
    
    def appending(self, number):
        self.lista.append(number)
        print(f"\nDodaje liczbe: {number}")

    def display_spaced(self):
        print("Podane liczby: ", end = '')
        for i in self.lista:
            print(i, end = ' ')
    
    def display_max(self):
        print(f"\nNajwiększa liczba to: {max(self.lista)}")
    
    def display_min(self):
        print(f"Najmniejsza liczba to: {min(self.lista)}")
    
    def average(self):
        print(f"Średnia arytmetyczna wynosi: {sum(self.lista)/len(self.lista)}")
    
    def median(self):
        print(f"Mediana wynosi: {statistics.median(self.lista)}")
        
staty = statystyka("12, 37, 6, 9, 17")
staty.display()
staty.appending(20)
staty.display_spaced()
staty.display_max()
staty.display_min()
staty.average()
staty.median()
