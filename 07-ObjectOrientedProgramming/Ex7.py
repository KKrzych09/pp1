class Student():
    
    licznik = 100000
    university = "UEK Kraków"
    
    def __init__(self, name, surname, major):
        self.name = name
        self.surname = surname
        self.major = major
        self.album = Student.licznik
        Student.licznik += 1
    
    def __str__ (self):
        return self.name + ' ' + self.surname.upper() + f" ({self.album})," + f"{self.major}," + Student.university
    
uczen1 = Student("Marian", "Kowalski", "Informatyka Stosowana")
print(uczen1)

uczen2 = Student("Stefan", "Nowak", "Informatyka Stosowana")
print(uczen2)