#2525 https://www.acmicpc.net/status?user_id=dpdls0228&problem_id=2525&from_mine=1

A, B = list(map(int, input().split()))
C = int(input())

if B + C < 60:
    print(A, B+C)
elif B + C >= 60:
    if A+((B+C)//60) >= 24:
        print(A+(B+C)//60-24, (B+C)%60)
    elif A+((B+C)//60) <= 23:
        print(A+(B+C)//60, (B+C)%60)