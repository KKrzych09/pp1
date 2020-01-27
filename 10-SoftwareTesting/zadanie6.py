from random import randint
class Macierz():
    
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.macierz = []
        
    def create_matrix(self):
        matrix = []
        matrix = [[randint(0,9) for i in range(self.n)] for j in range(self.m)]
            
        for row in matrix:
            print(row)
            
        self.macierz = matrix
    
    def __add__(self, other):
        if self.m == other.m and self.n == other.n:
            calculated_matrix = [[0 for i in range(self.n)] for j in range(self.m)]
            
            for a in range(len(self.macierz)):
                for b in range(len(self.macierz[0])):
                    calculated_matrix[a][b] = self.macierz[a][b] + other.macierz[a][b]
                       
            return calculated_matrix   
                       
        else:
            return "Macierzy nie mozna dodac bo nie sa tego samego wymiaru"
    

max1 = Macierz(4, 3)
max2 = Macierz(4, 3)

max1.create_matrix()
print("\n")
max2.create_matrix()
print("\n")
print(max1+max2)