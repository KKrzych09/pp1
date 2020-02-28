class Oceny():
    def __init__(self, tablica_ocen):
        self.tablica_ocen = tablica_ocen
        
    def __eq__(self, other):
        if sorted(self.tablica_ocen) == sorted(other.tablica_ocen):
            return "Studenci maja takie same oceny"
        else:
            return "Studenci nie maja takich samych ocen"
