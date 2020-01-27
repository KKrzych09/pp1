class Miasto():
    def __init__(self, nazwa, populacja):
        self.nazwa = nazwa
        self.populacja = populacja
    
    def __str__(self):
        str = 'Miasto '
        str += f'{self.nazwa}'
        str += f', populacja: {self.populacja}'
        
        return str

print(Miasto("Lubaczow", 13000))

    