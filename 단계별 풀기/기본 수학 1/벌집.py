n = int(input())

line = 1
r = 1

while r < n:
    r += 6 * line
    line += 1
print(line)