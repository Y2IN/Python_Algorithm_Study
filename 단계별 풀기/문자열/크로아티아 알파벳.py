##https://www.acmicpc.net/problem/2941
a = input()
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in c:
    a = a.replace(i, "~")
print(len(a))
