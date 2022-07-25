#https://www.acmicpc.net/problem/7568

n = int(input())
data = []
res = []
for i in range(n):
    weight, height = map(int, input().split())
    data.append((weight, height))

for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    res.append(count + 1)


for k in res:
    print(k, end = " ")