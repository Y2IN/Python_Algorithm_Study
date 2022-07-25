
import sys
n = int(input())

input = sys.stdin.readline

for i in range(n):
    A,B = list(map(int, input().split()))
    print(A+B)