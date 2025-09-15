# 1697 숨바꼭질 17: 00
# BFS (최단거리)
import sys
from collections import deque

input = sys.stdin.readline().strip().split()
if len(input) < 2:  
    print(0)

start_pos = int(input[0])
target_pos = int(input[1])

# 경계값: 문제 제약 범위 확인 (0..100000)
LIMIT = 100_000

if start_pos == target_pos:       # 이미 같은 위치면 0초
    print(0)

# 방문 겸 거리 테이블(최초 도달 시간이 최소) — -1이면 미방문
dist = [-1] * (LIMIT + 1)
dist[start_pos] = 0

q = deque([start_pos])
append = q.append
popleft = q.popleft

while q:
    cur = popleft()
    next_t = dist[cur] + 1

    # 다음 후보: cur-1, cur+1, cur*2
    for nx in (cur - 1, cur + 1, cur * 2):
        if 0 <= nx <= LIMIT and dist[nx] == -1:
            if nx == target_pos:  # 목표 최초 도달 = 최단시간
                print(next_t)
            dist[nx] = next_t
            append(nx)