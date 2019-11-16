income = int(input('Podaj dochód: '))
def podatek(dochod):
    if dochod <= 5000:
        return dochod * 0.17
    elif dochod > 5000:
        return (dochod - 5000) * 0.32 + 850
print(f'Podatek należny: {podatek(income)}zł')