#https://www.acmicpc.net/problem/11050

import math
n, k = map(int,input().split())
print(math.factorial(n)//(math.factorial(k) * math.factorial(n-k)))


"""
def factorial(n):
    if n<=1:
        return 1
    
    return n * factorial(n-1)
"""