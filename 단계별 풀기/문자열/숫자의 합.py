##https://www.acmicpc.net/problem/11720
N = int(input())
n = list(input())
s = 0
for i in range(N):
    s += int(n[i])
print (s)