##https://www.acmicpc.net/problem/2742

from re import I
import sys
input = sys.stdin.readline
n = int(input())

N = n
for i in range(1, n+1):
    N = n - i
    print(N+1)
    