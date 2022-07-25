##https://www.acmicpc.net/problem/4948

def prime(x):
    sqrt = int(x**(1/2)) 

    if x == 1:
        return False
    for j in range(2, sqrt+1):
        if x % j == 0:
            return False
    return True

limit = list(range(2,123456*2))
result = list()

for i in limit:
    if prime(i):
        result.append(i)

n = int(input()) 

while True:
    arr = []
    if n == 0:
        break
    for j in result:
        if n < j <= n * 2:
            arr.append(j)
    print(len(arr))
    n = int(input())