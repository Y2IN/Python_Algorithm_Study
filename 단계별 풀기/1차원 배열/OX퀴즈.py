##https://www.acmicpc.net/problem/8958

n = int(input())

for i in range(n):
    ox = list(input())
    score = 0
    sum_score = 0

    for check in ox:
        if check == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)