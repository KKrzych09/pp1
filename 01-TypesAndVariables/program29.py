import secrets


roll = secrets.randbelow(6) + 1
guess = 0

while guess != roll:
    guess = int(input("Guess: "))
    if guess != roll:
        print("Wrong!\n")
else:
    print("Correct!")