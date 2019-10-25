pin = ["0805"]

for i in range(0,3):
    insert_pin = str(input("Podaj kod PIN: "))
    if insert_pin == pin[0]:
        print("PIN jest poprawny.")
        break
    else:
        print("Nieprawidłowy pin.")
        if i == 2:
            print("Karta płatnicza zostaje zablokowana.")