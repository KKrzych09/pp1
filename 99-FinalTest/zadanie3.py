def jednostkowa(macierz):
    if len(macierz) == len(macierz[0]):
        for i in range(len(macierz)):
            for j in range(len(macierz[0])):
                if macierz[i][j] == 1:
                    return "Macierz jest jednostkowa"
                else:
                    return "Macierz nie jest jednostkowa"
        
    else:
        return "Macierz nie jest jednostkowa"
    