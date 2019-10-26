kwota = int(input("Podaj kwote w zł: "))

print(f"Kwota {kwota}zł w monetach: ")

jeden = 0
dwa = 0
piec = 0

x = kwota / 5
piec = int(x)

kwota = kwota - (int(x) * 5)
y = kwota / 2
dwa = int(y)

kwota = kwota - (int(y) * 2)
jeden = kwota

print(f"5 zł: {piec}szt")
print(f"2 zł: {dwa}szt")
print(f"1 zł: {jeden}szt")