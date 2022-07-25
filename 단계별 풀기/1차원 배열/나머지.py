##https://www.acmicpc.net/problem/3052

res = []

for i in range(10):
    n = int(input())
    n = n % 42
    res.append(n)

print(len(set(res)))