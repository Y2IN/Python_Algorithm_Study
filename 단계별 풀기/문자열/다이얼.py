

number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = list(input())
result = 0
for i in a:
    for j in number:
        if i in j:    
            result += number.index(j) + 3
print(result)
