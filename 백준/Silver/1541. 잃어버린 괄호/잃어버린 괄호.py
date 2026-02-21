import sys
input = sys.stdin.readline

temp = list(input().split('-'))
result = 0
arr = list(temp[0].split('+'))
for j in arr:
    result += int(j)
for i in range(1, len(temp)):

    arr = list(temp[i].split('+'))
    for j in arr:
        result -= int(j)

print(result)