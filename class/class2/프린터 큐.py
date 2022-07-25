#https://www.acmicpc.net/problem/1966


t = int(input())
for _ in range(t):
    count = 1
    N, M = map(int,input().split())
    important = list(map(int,input().split()))
    while True:
        if important[0] == max(important):
            if M == 0:
                print(count)
                break
            important.pop(0)
            M -= 1
            count += 1
        else:
            if M == 0:
                M = len(important) - 1
            else:
                M -= 1
            important.append(important[0])
            important.pop(0)
