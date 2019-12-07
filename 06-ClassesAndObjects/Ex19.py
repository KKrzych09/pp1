class bank_account():
    def __init__(self, account_nr):
        self.account_nr = account_nr
        self.saldo = 0
    
    def show_status(self):
        if len(self.account_nr) - self.account_nr.count(' ') == 26:
            print(f"Rachunek nr: {self.account_nr}")
            print(f"Saldo: {self.saldo}zł")
        else:
            print("Numer konta musi zawierać 26 cyfr!")
        
    def deposit(self, amount):
        self.saldo += float(amount)
        print(f"Wpłacono na konto: {amount}zł")
    
    def withdraw(self, amount):
        if amount > self.saldo:
            print(f"Niewystarczająca ilość środków na rachunku żeby wypłacić {amount}zł")
        else:
            self.saldo -= float(amount)
            print(f"Wypłacono z konta: {amount}zł")
        
            
nr_konta = bank_account("12 3456 5555 9090 1111 0000 7722")
nr_konta.show_status()
nr_konta.deposit(25.30)
nr_konta.show_status()
nr_konta.withdraw(31.70)
nr_konta.show_status()
nr_konta.withdraw(14)
nr_konta.show_status()


