#https://www.acmicpc.net/problem/11651

n = int(input())
arr = []

for _ in range(n):
    x, y = map(int,input().split())
    arr.append([y,x])

s_arr = sorted(arr)

for j in range(n):
    print(s_arr[j][1], s_arr[j][0])