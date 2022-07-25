## https://www.acmicpc.net/problem/1546

n = int(input())
score = (list(map(int, input().split())))
change_score = []
score_max = max(score)

for i in range(n):
    change_score.append(score[i]/score_max*100)

res = sum(change_score)/n
print(res)