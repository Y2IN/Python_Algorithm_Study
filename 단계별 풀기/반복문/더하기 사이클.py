##https://www.acmicpc.net/submit/1110

n = int(input())
nu = n
cycle = 0

while True:
    a = nu // 10
    b = nu % 10
    add = (a + b)%10
    nu = (b * 10) + add
    cycle += 1
    
    if(nu == n):
        break
print(cycle)