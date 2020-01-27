class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'P({self.x},{self.y})'
    
    def __eq__(self, other):
        if isinstance(other, Point):
            if self.x == other.x and self.y == other.y:
                return 'Odległość pomiędzy nimi wynosi 0'
            else:
                d = (((other.x - self.x) ** 2) + ((other.y - self.y) ** 2)) ** (1/2)
                return f'Odległość pomiędzy punktami wynosi {d}'
         

p1 = Point(3, 5)
p2 = Point(5, 8)

print(p1 == p2)

    