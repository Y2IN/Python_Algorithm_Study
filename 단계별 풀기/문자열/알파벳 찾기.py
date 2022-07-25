##https://www.acmicpc.net/problem/10809

s = input()
alpha = list(range(97,123))
for i in alpha:
    print(s.find(chr(i)), end = ' ')