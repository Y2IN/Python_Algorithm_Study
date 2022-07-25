##https://www.acmicpc.net/problem/2475
n = list(map(int, input().split()))
n_sum = 0
arr=[]

for i in n:
    n_sum += (i*i)
    
n_sum = n_sum % 10
print(n_sum)
