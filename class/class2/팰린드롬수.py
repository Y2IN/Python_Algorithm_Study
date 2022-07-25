#https://www.acmicpc.net/problem/1259

"""
while True:
    n = input()
    if n == "0":
        break
    
    res = "no"
    if n == n[::-1]:
        res = "yes"
    
    print(res)
"""

while True:
    flag = 1
    num = list(input())
    if num[0] == '0':
        break
    else:
        for i in range(len(num)//2):
            if num[i] == num[len(num)-1-i]:
                flag = 1
            else:
                flag = 0
                break
        if flag == 1:
            print("yes")
        else:
            print("no")    