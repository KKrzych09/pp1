class University():
    # konstruktor obiektu (metoda __init__)
    def __init__(self):
        # cechy obiektu (pola)
        self.name = 'UEK'
        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'
    # zachowania obiektu (metody)
    def print_name(self):
        print(self.name)
    
    def set_name(self, new_name):
       self.name = new_name
       print(new_name)
       
    def print_fullname(self):
        print(self.fullname)

    def set_fullname(self, new_name):
        self.fullname = new_name


uniwerek = University()
uniwerek.print_fullname()

uniwerek.set_fullname('Akademia Górniczo Hutnicza w Krakowie')
uniwerek.print_fullname()