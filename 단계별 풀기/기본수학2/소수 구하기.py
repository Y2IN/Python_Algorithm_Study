##https://www.acmicpc.net/problem/1929
M, N = map(int, input().split())

def prime(x):
    sqrt = int(x**(1/2)) + 1

    if x == 1:
        return False
    for j in range(2, sqrt):
        if x % j == 0:
            return False
    return True

for i in range(M, N+1):
    if prime(i):
        if i != 1:
            print(i)
    

