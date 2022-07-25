#https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

M = int(input())
M_list = set(map(int,input().split()))
N = int(input())
N_list = list(map(int, input().split()))

for i in N_list:
    if i in M_list:
        print(1)
    else:
        print(0)

