#https://www.acmicpc.net/problem/1181

n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

arr_lst = set(arr)
lst = list(arr_lst)
lst.sort()
lst.sort(key=len)

for i in lst:
    print(i)


    
