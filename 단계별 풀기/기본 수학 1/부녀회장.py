T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    people = [] 
    for j in range(1, n+1):
        people.append(j)
    for a in range(k): 
        for b in range(1, n): 
            people[b] += people[b-1] 
    print(people[-1])