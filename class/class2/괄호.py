#https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline

n = int(input())

for j in range(n):
    vps = input()
    s_list = list(vps)
    count = 0
    for i in s_list:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            print('NO')
            break
        
    if count > 0:
        print('NO')
    elif count == 0:
        print('YES')
        