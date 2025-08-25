# 막혀있는 것을 대비해서 캐릭터에 도달하지 못한다면 바로 -1로 반환 그러니 도착지점 주변에서
# 왼쪽과 바로 위쪽을 확인해서 0으로 되어있으면 -1을 반환
from collections import deque
from typing import List

# Type 명시
def solution(maps : List[List[int]]):
    answer = 0

    # 총 행, 열
    n_rows, n_cols = len(maps), len(maps[0])
    
    # 갈 수 있는 공간이 없어지므로 -1을 반환
    if maps[0][0] != 1 or maps[n_rows - 1][n_cols - 1] != 1:
        return -1
    
    # 시작=도착이 길
    if n_rows == 1 and n_cols == 1:
        return 1
    
    dist = [[0] * n_cols for _ in range(n_rows)]
    
    dist[0][0] = 1
    
    queue = deque([(0, 0)])
    
    # 델타
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        

    while queue:
        r, c = queue.popleft()

        # 도착 즉시 반환 (early exit)
        if r == n_rows - 1 and c == n_cols - 1:
            return dist[r][c]

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n_rows and 0 <= nc < n_cols:
                if maps[nr][nc] == 1 and dist[nr][nc] == 0:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

    # 도달 불가임
    return -1

