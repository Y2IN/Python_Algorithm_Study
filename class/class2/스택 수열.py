#https://www.acmicpc.net/problem/1874
 
import sys
input = sys.stdin.readline

N = int(input())
now = 1
stack = []
res = []
flag = True
for _ in range(N):
    num = int(input())
    while now <= num:
        stack.append(now)
        res.append('+')
        now += 1
        
    if stack[-1] == num:
        stack.pop()
        res.append('-')
    else:
        flag = False

if not flag:
    print('NO')
else:
    for i in res:
        print(i)

print(stack)
