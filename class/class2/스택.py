#https://www.acmicpc.net/problem/15829
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    a = input().split()
    if a[0] == "push":
        arr.append(a[1])
    elif a[0] == "top":
        if len(arr) == 0:
            print(-1) 
        else:
            print(arr[-1])
    elif a[0] == "size":
        print(len(arr))
    elif a[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())