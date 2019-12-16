class Vehicle():
    
    def __init__(self, brand, licence_number):
        self.brand = brand
        self.licence_number = licence_number
        self.is_rented = False
        self.mileage = 0
    
    
    def __str__(self):
        str = 'Samochód:'
        str += f'\nMarka: {self.brand}\n'
        str += f'Numer rejestracyjny: {self.licence_number}\n'
        str += f'Przebieg: {self.mileage}\n'

        if self.is_rented == False:
            str += f'Stan wypożyczenia: Dostępny\n\n'
        else:
            str += f'Stan wypożyczenia: Wypożyczony\n\n'
    
        return str
    
    
    def change_tenor(self, additional_mileage):
        self.tenor += additional_tenor
        
        
    def set_rent(self):
        self.is_rented = True
    
    
    def set_rented(self):
        self.is_renter = False


class Passenger_car(Vehicle):
    
    def __init__(self, brand, licence_number, spots):
        self.spots = spots
        super().__init__(brand, licence_number)
    
    
    def __str__(self):
        str = 'Samochód osobowy:' 
        str += f'\nMarka: {self.brand}\n'
        str += f'Numer rejestracyjny: {self.licence_number}\n'
        str += f'Przebieg: {self.mileage}\n'
        str += f'Ilość miejsc: {self.spots}\n'

        if self.is_rented == False:
            str += f'Stan wypożyczenia: Dostępny\n\n'
        else:
            str += f'Stan wypożyczenia: Wypożyczony\n\n'
    
        return str
        
    

class Delivery_van(Vehicle):
    
    def __init__(self, brand, licence_number, capacity):
        self.capacity = capacity
        super().__init__(brand, licence_number)
        
    def __str__(self):
        str = 'Samochód dostawczy:'
        str += f'\nMarka: {self.brand}\n'
        str += f'Numer rejestracyjny: {self.licence_number}\n'
        str += f'Przebieg: {self.mileage}\n'
        str += f'Ładowność: {self.capacity}t\n'

        if self.is_rented == False:
            str += f'Stan wypożyczenia: Dostępny\n\n'
        else:
            str += f'Stan wypożyczenia: Wypożyczony\n\n'
    
        return str


class Rental_store():
    
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.add_mileage = 0
        
    
    def __str__(self):
        str = self.name
        str += '\n\nLista wszystkich pojazdów: \n'
        for i in range(len(self.vehicles)):
            str += '-----------------------------\n'
            str += f'{i + 1}.{self.vehicles[i]}'
        return str

    
    def add_vehicle(self, new_car):
        self.vehicles.append(new_car)
        same_licence_number = list(filter(lambda car: car.licence_number == new_car.licence_number, self.vehicles))

        if len(same_licence_number) != 0:
            print("Nie możesz dodać pojazdu, samochód o takim numerze rejestracyjnym już istnieje!")

        
    
    
    def available_vehicles(self):
        
        print('Lista dostępnych pojazdów: ')
        
        for car in self.vehicles:
            if car.is_ranted == False:
                print(f'{i},{self.vehicles[i][0]}')
    
    
    def unavailable_vehicles(self):
        
        print('Lista pojazdów wypożyczonych: ')
        
        for car in self.vehicles:
            if car.is_ranted == True:
                print(f'{i},{self.vehicles[i][0]}')
    
    
    def return_vehicle(self, licence_number):
        
        self.add_mileage = int(input('Wprowadz liczbe przejechanych kilometrów: '))
        Vehicle.change_mileage(self.add_mileage)



wypozyczalnia = Rental_store("Rent Cars")


wypozyczalnia.add_vehicle(Passenger_car('BMW E36', 'KR 1908', 5))
wypozyczalnia.add_vehicle(Passenger_car('Opel Omega', 'KR 1908', 5))
wypozyczalnia.add_vehicle(Passenger_car('Ford Mustang', 'KR 9083', 4))
wypozyczalnia.add_vehicle(Delivery_van('Volkswagen Transporter', 'KR 2948', 2.5))
wypozyczalnia.add_vehicle(Delivery_van('Mercedes Sprinter', 'KR 4248', 3.5))

print(wypozyczalnia)

        
        
        
        
