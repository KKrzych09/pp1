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
    def create_unit(x):
        unit_matrix = matrix.create(x,x)
        
        for i,row in enumerate(unit_matrix, 0):
            unit_matrix[i][i] = 1
            print(row)
        

m_unit = matrix.create_unit(5)
