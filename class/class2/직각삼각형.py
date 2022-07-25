#https://www.acmicpc.net/problem/4153

while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    arr = [a,b,c]
    arr.sort()
    if arr[0] ** 2 + arr[1] **2 == arr[2] ** 2:
        print("right")
    else:
        print("wrong")


"""
while True :
  a, b, c = map(int, input().split())
  if a==0 and b==0 and c==0 :
    break
  
  a *= a
  b *= b
  c *= c
  if a+b == c or a+c == b or b+c == a :
    print("right")
  else :
    print("wrong")
"""