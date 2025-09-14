# 1920 수 찾기 21: 00

import sys

input = sys.stdin.readline

N = int(input())

A = set(map(int, input().split())) # 탐색시간을 줄이기 위해 중복을 최소화

M = int(input())

AM = list(map(int, input().split()))

# A안에 AM 요소가 있으면 1, 없으면 0
# result = []
for am in AM:
    if am in A:
        # result.append(1)
        print(1)
    else:
        # result.append(0)
        print(0)
        
# for _ in result:
#     print(_)