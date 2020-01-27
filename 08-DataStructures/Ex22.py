import random
class matrix():

    @staticmethod
    def create(x,y):
        value = 0
        matrix = [[value for i in range(y)] for j in range(x)]
        return matrix

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
            
    
    @staticmethod
    def compare(matrix1, matrix2):
        if len(matrix1) == len(matrix2) and (len(matrix1[0]) / len(matrix1)) == (len(matrix2[0]) / len(matrix2)):
            print("Macierze są takiego samego wymiaru.")
            
            counter = 0
            for i in range(len(matrix1)):
                    for j in range(len(matrix1[0])):
                        if matrix1[i][j] == matrix2[i][j]:
                            counter += 1
                        else:
                            pass
                        
            if len(matrix1) ** 2 == counter:
                print("Macierze mają takie same wartości")
            else:
                print("Macierze nie mają takich samych wartości")
                
        else:
            print("Macierze nie sią tego samego wymiaru.")
                

mat1 = matrix.create(3, 3)
mat2 = matrix.create(3, 3)

matrix.print(mat1)
matrix.print(mat2)

matrix.compare(mat1, mat2)