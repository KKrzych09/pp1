import random

class dice():
    def __init__(self):
        self.number = random.randint(1,6)
        self.suma = 0
        
    def rolling(self):
        print(self.number)
        
kostka1 = dice()
kostka1.rolling()
sum = kostka1.number
print(f"Suma oczek: {sum}")

kostka2 = dice()
kostka2.rolling()
sum += kostka2.number
print(f"Suma oczek: {sum}")

kostka3 = dice()
kostka3.rolling()
sum += kostka3.number
print(f"Suma oczek: {sum}")
