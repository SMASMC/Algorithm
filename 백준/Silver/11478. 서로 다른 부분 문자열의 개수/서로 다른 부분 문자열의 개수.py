# 20: 20 서로 다른 부분 문자열의 개수 11478
import sys

S = sys.stdin.readline().rstrip()

cnt = set()

for i in range(0, len(S)):
    for j in range(i, len(S)):
        cnt.add(S[i:j+1])

print(len(cnt))