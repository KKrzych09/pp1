from random import randint
class Two_arrays():
    
    @staticmethod
    def ten_elements():
        ten_tab = []
        for i in range(10):
            ten_tab.append(4)
        print(ten_tab)
    
    @staticmethod
    def twenty_elements():
        twenty_tab = []
        amount = 0
        for i in range(20):
            twenty_tab.append(randint(-7, 8))
        print(twenty_tab)
        
        for j in twenty_tab:
            if j >= -1 and j <= 1:
                amount += 1
        print(f'Liczba wartosci z przedzialu <-1, 1> wynosi {amount}')
        
        
Two_arrays.ten_elements()
Two_arrays.twenty_elements()
