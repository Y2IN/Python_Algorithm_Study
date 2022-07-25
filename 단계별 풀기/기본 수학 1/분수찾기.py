##https://www.acmicpc.net/problem/1193

X = int(input())
n = 1

while n < X:
    X -= n
    n += 1

if n % 2 == 1:
    print("%d/%d" % (n-X+1, X))
else:
    print("%d/%d" % (X,n-X+1))