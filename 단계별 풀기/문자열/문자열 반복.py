##https://www.acmicpc.net/problem/2675

T = int(input())

for i in range(T):
    A,B = input().split()
    A = int(A)
    B = str(B)

    for i in range(len(B)):
        print(A*B[i], end='')
    print()

