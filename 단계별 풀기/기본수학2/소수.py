##https://www.acmicpc.net/problem/2581


def prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True


M = int(input())
N = int(input())
arr = []

for j in range(M, N+1):
    if prime(j):
        if j != 1:
            arr.append(j)

if not arr:
    print(-1)

else:
    print(sum(arr))
    print(min(arr))
