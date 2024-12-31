fib_cache = {}

def fib(n):
    if n in fib_cache:
        return fib_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fib(n-1) + fib(n-2)

    fib_cache[n] = value
    return value

for n in range(1,20001):
    print(n, ":", fib(n))
