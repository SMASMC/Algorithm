# 14425 문자열 집합 23: 05

# N개 안에 M개로 입력한 값들 중에서 N개 안에 포함되는 집합 S는 얼마인가?

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

S = []
cnt = 0
for _ in range(N):
    S.append(input()) # 집합을 생성

for _ in range(M):
    chr_M = input()
    if chr_M in set(S):
        cnt += 1
        
print(cnt)