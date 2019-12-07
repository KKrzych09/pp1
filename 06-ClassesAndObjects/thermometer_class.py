import random
class termometr():
    def __init__(self):
        self.temperatura = 0
        self.is_on = False
    
    def on(self):
        self.is_on = True
        print("Termometr jest włączony.")
        
    def off(self):
        self.is_on = False
        print("Termometr jest wyłączony.")
        
    def zmierz_temperature(self):
        if self.is_on == True:
            self.temperatura = random.uniform(34.0,42.0)
            print(f"Zmierzona temperatura: {round(self.temperatura, 1)} ", end = '')
            if self.temperatura > 37.0 and self.temperatura < 41.0:
                print("(gorączka)")
            elif self.temperatura > 41.0:
                print("(stan zagrożenia zycia!!!)")
            else:
                print("(temperatura w normie)")
        else:
            print("Najpierw musisz włączyć termometr.")