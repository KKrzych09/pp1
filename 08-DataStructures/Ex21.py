import random
class matrix():

    @staticmethod
    def create(x,y):
        matrix = []
        value = 0
        for i in range(x):
            # create single row
            row = []
            for j in range(y):
                row.append(value)
            # add row to matrix
            matrix.append(row)
        return matrix

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
    
    @staticmethod
    def create_diagonally(x):
        diagonally_matrix = matrix.create(x,x)
        
        for i,row in enumerate(diagonally_matrix, 0):
            diagonally_matrix[i][i] = random.randint(10,50)
            print(row)

m = matrix.create_diagonally(4)
