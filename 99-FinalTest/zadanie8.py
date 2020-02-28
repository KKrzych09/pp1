class Termometr():
    def __init__(self, ile_pomiarow):
        self.ile_pomiarow = ile_pomiarow
        self.temperatury = []
        
    def rejestruj(self, temperatura):
        self.temperatury.append(temperatura)
        if len(self.temperatury) > self.ile_pomiarow:
            self.temperatury.pop(0)
        
    def temp_last(self):
        return f"Ostatnio zarejestrowana temperatura wynosi {self.temperatury[self.ile_pomiarow - 1]}"
    
    def temp_min(self):
        return f"Minimalna temperatura wynosi: {min(self.temperatury)}"
    
    def temp_max(self):
        return f"Maksymalna temperatura wynosi: {max(self.temperatury)}"
    