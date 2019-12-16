class Arrays():
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    
    @staticmethod
    def print_with_comma(array):
        comma = ', '.join(map(str, array))
        for i in comma:
            print(i, end = '')
            
my_array = [4,1,8,7,2]
Arrays.print_in_col(my_array)
Arrays.print_with_comma(my_array)