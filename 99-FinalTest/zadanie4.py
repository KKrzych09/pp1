class Tekst():
    
    @staticmethod
    def ukryj(tekst):
        result = ""
        if len(tekst) >= 3:
            for i in range(3):
                result += tekst[i]
            result += "*" * (len(tekst) - 3)
            return result
        else:
            return "Tekst ma mniej niz 3 znaki"
        
    @staticmethod
    def policz(tekst):
        counter = 0
        for i in tekst.split(" "):
            counter += 1
        return counter
    