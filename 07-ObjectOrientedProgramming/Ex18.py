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
        str += f'Przebieg: {self.mileage}km\n'

        if self.is_rented == False:
            str += f'Stan wypożyczenia: Dostępny\n\n'
        else:
            str += f'Stan wypożyczenia: Wypożyczony\n\n'
    
        return str
    
    
    def change_mileage(self, additional_mileage):
        self.mileage += additional_mileage
        
        
    def set_rent(self):
        self.is_rented = True
    
    
    def set_rented(self):
        self.is_rented = False


class Passenger_car(Vehicle):
    
    def __init__(self, brand, licence_number, spots):
        super().__init__(brand, licence_number)
        self.spots = spots
    
    
    def __str__(self):
        str = 'Samochód osobowy:' 
        str += f'\nMarka: {self.brand}\n'
        str += f'Numer rejestracyjny: {self.licence_number}\n'
        str += f'Przebieg: {self.mileage}km\n'
        str += f'Ilość miejsc: {self.spots}\n'

        if self.is_rented == False:
            str += f'Stan wypożyczenia: Dostępny\n\n'
        else:
            str += f'Stan wypożyczenia: Wypożyczony\n\n'
    
        return str
        
    
class Delivery_van(Vehicle):
    
    def __init__(self, brand, licence_number, capacity):
        super().__init__(brand, licence_number)
        self.capacity = capacity

        
    def __str__(self):
        str = 'Samochód dostawczy:'
        str += f'\nMarka: {self.brand}\n'
        str += f'Numer rejestracyjny: {self.licence_number}\n'
        str += f'Przebieg: {self.mileage}km\n'
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
        
        same_licence_number = list(filter(lambda car: car.licence_number == new_car.licence_number, self.vehicles))

        if len(same_licence_number) != 0:
            print(f"Nie możesz dodać pojazdu o numerze {new_car.licence_number}, bo taki już istnieje!")
        else:
            self.vehicles.append(new_car)
    
    
    def available_vehicles(self):
        counter = 1
        print('\nLista dostępnych pojazdów: \n')
        
        for i, car in enumerate(self.vehicles, 0):
            if car.is_rented == False:
                print('-----------------------------')
                print(f'{counter}.{self.vehicles[i]}')
                counter += 1
    
    
    def unavailable_vehicles(self):
        counter = 1
        print('\nLista pojazdów wypożyczonych: \n')
        
        for i, car in enumerate(self.vehicles, 0):
            if car.is_rented == True:
                print('-----------------------------')
                print(f'{counter}.{self.vehicles[i]}')
                counter += 1
    
    
    def rent_vehicle(self, licence_number):
        
        for i, car in enumerate(self.vehicles, 1):
            if car.licence_number == licence_number:
                actual_car = car
                
                actual_car.is_rented = True
                print(f'Wypożyczam samochód o numerze rejestracyjnym {licence_number}...\n')
                break
            elif i == len(self.vehicles):
                print(f'Nie ma pojazdu o numerze {licence_number}.\n')
                
    
    def return_vehicle(self, licence_number):
        
        for i, car in enumerate(self.vehicles, 1):
            if car.licence_number == licence_number:
                actual_car = car
                
                actual_car.is_rented = False
                print(f'Zwracam samochód o numerze rejestracyjnym {licence_number}...')
                break
            elif i == len(self.vehicles):
                print(f'Nie ma pojazdu o numerze {licence_number}.\n')
            
        self.add_mileage = int(input('Wprowadz liczbe przejechanych kilometrów: '))
        actual_car.change_mileage(self.add_mileage)


wypozyczalnia = Rental_store("Rent Cars")

wypozyczalnia.add_vehicle(Passenger_car('BMW E36', 'KR 1908', 5))
wypozyczalnia.add_vehicle(Passenger_car('Opel Omega', 'KR 1212', 5))
wypozyczalnia.add_vehicle(Passenger_car('Ford Mustang', 'KR 9083', 4))
wypozyczalnia.add_vehicle(Delivery_van('Volkswagen Transporter', 'KR 2948', 2.5))
wypozyczalnia.add_vehicle(Delivery_van('Mercedes Sprinter', 'KR 4248', 3.5))

print(wypozyczalnia)

wypozyczalnia.rent_vehicle('KR 9083')
wypozyczalnia.rent_vehicle('KR 2948')

wypozyczalnia.unavailable_vehicles()

wypozyczalnia.available_vehicles()

wypozyczalnia.return_vehicle('KR 9083')

wypozyczalnia.unavailable_vehicles()

wypozyczalnia.available_vehicles()
