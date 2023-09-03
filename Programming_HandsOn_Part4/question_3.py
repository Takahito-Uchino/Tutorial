def fib(n):
    a = 1
    b = 1
    while a <= n:
        print(a, end = ' ')
        tmp = a
        a = b
        b = tmp + a
fib(100000)