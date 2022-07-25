#https://www.acmicpc.net/problem/1436
"""
n = int(input())
first = 666

while n != 0:
    if '666' in str(first):
        n -= 1
        if n == 0:
            break

    first = first + 1
print(first)
"""

n = int(input())

first = 666
cnt = 0
while True:
    if '666' in str(first):
        cnt += 1
    if cnt == n:
        print(first)
        break
    first += 1     




