class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    
    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
        
    def show_status(self):
        print(f"Telewizor jest załączony i ustawiony jest kanał {self.channel_no}({self.channels[self.channel_no - 1]}) głośność jest ustawiona na: {self.volume}" if self.is_on else "Telewizor jest wyłączony")
    
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    
    def set_channels(self, channels_list):
        for i in channels_list:
            self.channels.append(i)
        
    def show_channels(self):
        print(f'Lista dostępnych programów: {self.channels}')
        
    def volume_up(self):
        if self.volume < 10:
            self.volume += 1
    
    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1

tv = TV()
tv.on()
tv.set_channels(['TVP1', 'TVP2', 'POLSAT', 'TVN', 'Filmbox', 'Eurosport', 'Jetix'])
tv.show_channels()
tv.show_status()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.set_channel(3)
tv.show_status()
tv.volume_down()
tv.volume_down()
tv.set_channel(6)
tv.show_status()
