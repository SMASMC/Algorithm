# 7569 토마토 22: 50

import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

box = []
queue = deque()
count = 0

# 입력: H층 × N행
for h in range(H):
    layer = []
    for _ in range(N):
        row = list(map(int, input().split()))
        layer.append(row)
    box.append(layer)

# 시작점(익은 토마토) 수집 + 안 익은 개수 집계
for h in range(H):
    for r in range(N):
        for c in range(M):
            if box[h][r][c] == 1:
                queue.append((h, r, c))
            elif box[h][r][c] == 0:
                count += 1

# 모두 이미 익어있으면 0일
if count == 0:
    print(0)
    exit()

dirs = ((1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1))
max_day = 1  # 박스에 기록되는 최소 시작값(1)

while queue:
    z, y, x = queue.popleft()
    current_day = box[z][y][x]

    for dz, dy, dx in dirs:
        nz, ny, nx = z + dz, y + dy, x + dx
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = current_day + 1  # 하루 뒤에 익음
                count -= 1
                max_day = max(max_day, box[nz][ny][nx])
                queue.append((nz, ny, nx))

# 아직 안 익은 게 남아 있으면 -1
if count > 0:
    print(-1)
    exit()

# 기록은 1부터 시작했으니 일수는 -1
print(max_day - 1)