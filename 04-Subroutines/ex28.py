jezyki = ['Java','Python','JavaScript','C++','C#','Ruby','Perl','PHP','C','Android']
wartosciJezykow = [28,19,10,8,6,5,4,4,2,1]
def wykres(jezyk, wartosci):
    i = 0
    while i < len(jezyk):
        print(f'{jezyk[i]}: ' + '#' * wartosci[i])
        i += 1
wykres(jezyki,wartosciJezykow)  