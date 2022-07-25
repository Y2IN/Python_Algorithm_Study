##https://www.acmicpc.net/problem/10818
import sys
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

print(n_list[0], n_list[n-1])