from random import randint
class arrays():
    
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    
    @staticmethod
    def create_array(liczba_elementow_tablicy, wartosc_elementow_tablicy):
        new_array = [] 
        for i in range(liczba_elementow_tablicy):
            new_array.append(wartosc_elementow_tablicy)
        print(new_array)
    
    @staticmethod
    def new_random_array(liczba_elementow_tablicy, wartosc_od, wartosc_do):
        random_array = []
        for i in range(liczba_elementow_tablicy):
            random_array.append(randint(wartosc_od, wartosc_do))
        print(random_array)
    
    @staticmethod
    def arrays_elements(tablica, wartosc_od, wartosc_do):
        for i in range(randint(1, 100)):
            tablica.append(randint(wartosc_od, wartosc_do))
        print(tablica)
        print(f'Długość tablicy wynosi: {len(tablica)}')
    
    @staticmethod
    def delimeter():
        comma = ', '.join(map(str, my_array))
        print(comma)
    
    @staticmethod
    def change_delimeter(character):
        sign = character.join(map(str, my_array))
        print(sign)
            
my_array = [4,1,8,7,2]
arrays.print_in_col(my_array)
arrays.create_array(10, 5)
arrays.new_random_array(10, 1, 90)
arrays.arrays_elements([], 1, 20)
arrays.delimeter()
arrays.change_delimeter('/')
