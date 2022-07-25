##https://www.acmicpc.net/problem/9020


def prime(x):
    sqrt = int(x**(1/2))

    if x == 1:
        return False
    for j in range(2, sqrt + 1):
        if x % j == 0:
            return False
    return True


primes = []

for a in range(2, 10000):
    if prime(a): 
        primes.append(a)

T = int(input())
for i in range(T):
    n = int(input())
    half = n // 2

    for i in range(half, 1, -1):
        if (half in primes) and ((n-half) in primes):
            print(half, (n-half))
            break
        half -= 1




