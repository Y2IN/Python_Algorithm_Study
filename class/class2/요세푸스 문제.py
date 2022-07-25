#https://www.acmicpc.net/problem/11866

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num_list = [i for i in range(1, n+1)]
cnt = 1
arr = []
while num_list:
    if cnt == k:
        arr.append(num_list.pop(0))
        cnt = 1
    else:
        num_list.append(num_list.pop(0))
        cnt += 1



print('<'+', '.join(str(i)for i in arr)+'>')
    