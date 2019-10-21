login = "marek"
password = "m-123"

dane1 = str(input("Wprowadz login: "))
dane2 = str(input("Wprowadz haslo: "))
            
if dane1 == login and dane2 == password:
    print("Pomyslnie zalogowano.")
else:
    print("Dane sa nieprawidlowe.")