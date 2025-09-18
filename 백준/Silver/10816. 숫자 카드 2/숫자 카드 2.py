# 10816 숫자 카드 2 17: 00
import sys

input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
checks = list(map(int, input().split()))

dict1 = {}
for x in cards:
    if x in dict1:
        dict1[x] += 1
    else:
        dict1[x] = 1

for element in checks:
    if element in dict1:
        print(dict1[element], end=' ')
    else:
        print(0, end=' ')