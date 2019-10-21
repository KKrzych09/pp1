import secrets

rolls = [0] * 3
rolls_sum = 0

for roll in rolls:
    roll = secrets.randbelow(6) + 1
    print(f"Rolled: {roll}")
    rolls_sum += roll

print(f"Sum of rolls: {rolls_sum}")