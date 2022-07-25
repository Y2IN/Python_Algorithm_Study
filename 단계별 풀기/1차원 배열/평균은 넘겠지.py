##https://www.acmicpc.net/problem/4344

c = int(input())

for i in range(c):
    N_list = list(map(int, input().split()))
    N = N_list[0]
    score = N_list[1:]
    average = sum(score) / N
    up = []
    for j in score:
        if j > average:
            up.append(j)
    result = len(up) / N*100
    print("{:.3f}".format(result)+'%')