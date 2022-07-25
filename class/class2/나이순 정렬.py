#https://www.acmicpc.net/problem/10814


n = int(input())
p_arr = []
for _ in range(n):
    age, name = input().split()
    age = int(age)
    p_arr.append([age, name])
p_arr.sort(key=lambda x: x[0])

for i in p_arr:
    print(i[0], i[1], sep = ' ')



