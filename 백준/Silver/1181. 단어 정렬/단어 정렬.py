import sys

input = sys.stdin.readline

n = int(input())

data = []
for i in range(n):
    data.append(input().strip())    
data = list(set(data))
data.sort()
data = sorted(data, key = len)

for a in data:
    print(a)