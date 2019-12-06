class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
    
    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
        
    def show_status(self):
        print(f"Telewizor jest załączony i ustawiony jest kanał {self.channel_no}" if self.is_on else "Telewizor jest wyłączony")
    
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

tv = TV()
tv.show_status()
tv.on()
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.off()
tv.show_status()