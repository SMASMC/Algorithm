# 8979 올림픽

import sys

input = sys.stdin.readline

# 금은동 모두 같으면 같은 등수 / 은, 동이 서로 다르면 높은 국가가 높은 등수
# 금, 은, 동의 정보를 입력받고 몇등인지 알려주는 프로그램

N, K = map(int, input().split())

medals = [list(map(int, input().split())) for _ in range(N)]
    
medals.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

idx = [medals[i][0] for i in range(N)].index(K)

for i in range(N):
    if medals[idx][1:] == medals[i][1:]:
        print(i+1)
        break