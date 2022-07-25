#https://www.acmicpc.net/problem/4949


while True:
    sen = input()
    if sen == ".":
        break
    arr = []
    temp = True
    for i in sen:
        if i == '(' or i =='[':
            arr.append(i)
        elif i == ')':
            if not arr or arr[-1] == '[':
                temp = False
                break
            elif arr[-1] == '(':
                arr.pop()
        elif i == ']':
            if not arr or arr[-1] == '(':
                temp = False
                break
            elif arr[-1] == '[':
                arr.pop()
    if temp == True and not arr:
        print('yes')
    else:
        print('no')