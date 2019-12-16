class Mobile():
    
    def __init__(self):
        self.if_lock = True
    
    def __str__(self):
        if self.if_lock == True:
            return 'Telefon jest zablokowany.'
        else:
            return 'Telefon jest odblokowany.'
    
    def lock_phone(self):
        print('Blokuję telefon...')
        self.if_lock = True
    
    def unlock_phone(self):
        print('Odblokowywuję telefon...')
        self.if_lock = False

telefon1 = Mobile()
telefon2 = Mobile()

print(telefon1)
telefon1.unlock_phone()
print(telefon1)
print('\n')
print(telefon2)
telefon2.unlock_phone()
print(telefon2)
