def fib(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b,a+b
    return a
print('20 pierwszych wyrazów ciagu Fibonacciego: ', end = '')
for i in range(1,20):
    print(fib(i), end = ' ')