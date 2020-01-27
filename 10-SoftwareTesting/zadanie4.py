class Zbiory():
    
    @staticmethod
    def iloczyn(zbior1, zbior2):
        result = []
        if len(zbior1) > len(zbior2):           
            for num1 in zbior1:
                for num2 in zbior2:
                    if num1 == num2:
                        result.append(num1)
            return result
    
        elif len(zbior1) == len(zbior2):
            for num1 in zbior1:
                for num2 in zbior2:
                    if num1 == num2:
                        result.append(num1)
            return result
            
        else:
            for num2 in zbior2:
                for num1 in zbior1:
                    if num1 == num2:
                        result.append(num1)
            return result
        
    @staticmethod
    def suma(zbior1, zbior2):
        return zbior1 + zbior2
        
    @staticmethod
    def roznica(zbior1, zbior2):
        halfResult = []
        for num1 in zbior1:
                for num2 in zbior2:
                    if num1 == num2:
                        halfResult.append(num1)
        
        for i in halfResult:
            for num1 in zbior1:
                if num1 == i:
                    zbior1.remove(num1)
        return zbior1
        
        