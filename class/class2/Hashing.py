#https://www.acmicpc.net/problem/15829

n = int(input())
str_l = list(input())
res = 0

for i in range(n):
    res += ((ord(str_l[i]) -  96) * 31 ** i)

print (res%1234567891)