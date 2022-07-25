##https://www.acmicpc.net/problem/10871

N,X = list(map(int, input().split()))

a =list(map(int, input().split()))

for i in range(N):
    if a[i] < X:
        print(a[i], end=' ')