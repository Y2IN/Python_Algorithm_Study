#https://www.acmicpc.net/problem/2609
import sys
import math
input = sys.stdin.readline
m, n = map(int, input().split())
"""
for i in range(min(a,b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

for j in range(max(a,b), (a*b)+1):
    if j % a == 0 and j % b == 0:
        print(j)
        break
"""
"""
print(math.gcd(a,b))
print(math.lcm(a,b))
"""

def gcd(a,b):
    a,b = max(a,b), min(a,b)
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(m,n))
print(m*n//gcd(m,n))


