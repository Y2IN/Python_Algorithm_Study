#https://www.acmicpc.net/problem/11866
from collections import deque
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
stack = deque([i for i in range(1, n+1)])

print("<", end="")
while stack:
    stack.rotate(-(k-1))
    print(stack.popleft(),end="")
    if stack:
        print(",",end=" ")
print(">",end="")
"""

dq = deque('apple')


dq.rotate(2)
# deque(['a', 'e', 'l', 'p', 'p'])

print(dq)