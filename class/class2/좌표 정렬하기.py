
n = int(input())

arr = []
for i in range(n):
    [x,y] = map(int,input().split())
    arr.append([x,y])

#arr.sort()
s_arr = sorted(arr)
for j in s_arr:
    print(j[0], j[1])