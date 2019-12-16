import message
class E_mail(message.Message):
    def __init__(self, sender_email, recipient_email, subject):
        self.sender_email = sender_email
        self.recipient_email = recipient_email
        self.subject = subject
        super().__init__()
    
    def send(self):
        print("Wysyłanie emaila...")
        print(f"{'Od: ':<7} {self.sender_email}")
        print(f"{'Do: ':<7} {self.recipient_email}")
        print(f"{'Temat: ':<7} {self.subject}")
        print(f"{'Treść: ':<7} {self.message} \n")