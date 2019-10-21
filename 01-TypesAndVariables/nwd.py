import math

x, y = int(input("First num: ")), int(input("Second num: "))
print(f"Największy wspólny dzielnik ({x}, {y}) = {math.gcd(x, y)}")