##https://www.acmicpc.net/problem/2908

##num1, num2 = map(int, input().split())
##num1_list = list(map(int,str(num1)))
##num2_list = list(map(int,str(num2)))

##num1 = num1_list[2]*100 + num1_list[1]*10 + num1_list[0]
##num2 = num2_list[2]*100 + num2_list[1]*10 + num2_list[0]

##if int(num1) > int(num2):
##    print(num1)
##elif int(num1) < int(num2):
##    print(num2)

num1, num2 = input().split()
num1_list = list(num1)
num2_list = list(num2)

num1_list.reverse()
num2_list.reverse()

a = int(num1_list[0]+num1_list[1]+num1_list[2])
b = int(num2_list[0]+num2_list[1]+num2_list[2])

if a>b:
    print(a)
else:
    print(b)
