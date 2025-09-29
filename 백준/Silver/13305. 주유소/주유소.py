# 13305 주유소 18:40

import sys

input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
A = price[0]

for i in range(N-1):
    if price[i] < A:
        A = price[i]
    result += A*dist[i]

print(result)