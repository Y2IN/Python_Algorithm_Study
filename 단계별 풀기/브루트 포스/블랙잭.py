##https://www.acmicpc.net/problem/2798

n, m = list(map(int, input().split()))
card = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = card[i] + card[j] + card[k]
            if (sum <= m and sum > result):
                result = sum


print(result)
