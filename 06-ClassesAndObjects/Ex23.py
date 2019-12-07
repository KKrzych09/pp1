class kontakt():
    def __init__ (self, nazwa, email, telefon):
        self.nazwa = nazwa
        self.email = email
        self.telefon = telefon   
    
class kontaktow_lista():
    def __init__ (self):
        self.lista_kontaktow = []
        
    
    def dodaj_kontakt(self, nazwa, email, telefon):
        kontakty = kontakt(nazwa, email, telefon)
        self.lista_kontaktow.append(kontakty)
    
    def display(self):
        for i in self.lista_kontaktow:
             print(f"{i.nazwa:<20}" + f"{i.email:<20}" + f"{i.telefon:<20}")

wynik = kontaktow_lista()
wynik.dodaj_kontakt("Kowalski Jan","jank@onet.pl","555234000")
wynik.dodaj_kontakt("Borek Patrycja","bp@o2.pl","232000199")
wynik.dodaj_kontakt("Maj Piotr","maj@google.pl","222999100")
wynik.dodaj_kontakt("Adamczyk Anna","ada@poczta.pl","1002003000")
wynik.display()