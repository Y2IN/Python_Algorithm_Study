##https://www.acmicpc.net/problem/1978

def prime(x):
    for i in range(2, x)
        if x % i == 0:
            return False
    return True


N = int(input())
primes = map(int, input().split())
arr = []

for i in primes:
    if prime(i):
        if i != 1:
            arr.append(i)
print(len(arr))