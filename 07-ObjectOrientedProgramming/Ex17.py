import math
class Calculation():
    
    @staticmethod
    def triangle(basis, height):
        area = (basis * height) / (1/2)
        print(f"Area of your triangle is: {area}")
    
    @staticmethod
    def rectangle(length, height):
        area = length * height
        print(f"Area of your rectangle is: {area}")
    
    @staticmethod
    def circle(radius):
        area = (math.pi * radius) ** 2
        print(f"Area of your circle is: {area}")

Calculation.triangle(6, 2)
Calculation.rectangle(4, 7)
Calculation.circle(3)