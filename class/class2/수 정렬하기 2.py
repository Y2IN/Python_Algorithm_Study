#https://www.acmicpc.net/problem/2751
import sys
input = sys.stdin.readline

arr = []
s_arr = []
for _ in range(int(input())):
    arr.append(int(input()))
s_arr = sorted(arr)


for i in s_arr:
    print(i)