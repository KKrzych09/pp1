def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    
print("20 pierwszych wyrazów ciągi Fibonacciego: ")
for i in range(20):
    print(fibonacci(i), end = ' ')