def factoriel(n):
    if n == 0:
        return 1
    return n * factoriel(n-1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def syracuse(T):
    print(T)
    if T == 1:
        return
    elif T % 2 == 0:
        syracuse(T/2)
    else:
        syracuse(3*T+1)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)