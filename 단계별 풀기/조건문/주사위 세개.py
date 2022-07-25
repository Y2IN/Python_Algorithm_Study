##2480 https://www.acmicpc.net/submit/2480

A,B,C = list(map(int, input().split()))

if A == B == C:
    print(10000 + (1000*A))
elif (A == B) or (A == C) or (B == C):
    if A == B or A == C:
        print(1000 + (A*100))
    elif B == C:
        print(1000 + (B*100))
elif (A!=B) and (A!=C) and (B!=C):
    print(max(A,B,C)*100)
