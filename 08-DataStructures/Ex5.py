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

m = matrix.create(4,3)
matrix.print(m)