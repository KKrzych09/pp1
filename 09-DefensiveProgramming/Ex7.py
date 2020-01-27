height = float(input("Podaj swoj wzrost w centymetrach: "))
weight = float(input("Podaj swoja wage w kilogramach: "))

assert type(height) == int and height >= 150 and height <= 220
assert weight >= 40.0 and weight <= 150.0

bmi = weight / (pow(height, 2))
print("Twoj wskaznik BMI wynosi: {}".format(bmi))
