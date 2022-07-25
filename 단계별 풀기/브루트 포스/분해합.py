##https://www.acmicpc.net/problem/2231

n = int(input())
result = 0
for i in range(n):
    a = list(map(int, str(i)))
    result = i + sum(a)
    if result == n:
        print(i)
        break

    if i == n:
        print(0)

