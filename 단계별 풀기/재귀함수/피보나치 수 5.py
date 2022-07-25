##https://www.acmicpc.net/problem/10870

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


A = int(input())
print (fibonacci(A))
