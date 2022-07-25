##https://www.acmicpc.net/problem/11653

n = int(input())

i = 2
while i <= n:
    while n % i == 0:
        n /= i
        print(i)
    i = i + 1   