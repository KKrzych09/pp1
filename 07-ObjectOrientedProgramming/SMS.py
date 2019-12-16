import message
class Sms(message.Message):
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        super().__init__()
    
    def send(self):
        print("Wysyłanie SMS-a...")
        print(f"{'Od: ':<7} {self.sender}")
        print(f"{'Do: ':<7} {self.recipient}")
        print(f"{'Treść: ':<9} {self.message} \n")