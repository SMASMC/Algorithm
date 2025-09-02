# 14891 톱니바퀴 - deque 회전 + 방향 전파
import sys
from collections import deque


input = sys.stdin.readline

# 4개의 톱니 (각각 길이 8, '0': N, '1': S)
gears = [deque(input().strip()) for _ in range(4)]
k = int(input())

# 접점 인덱스(회전 전 상태 기준으로 비교)
RIGHT_TOOTH = 2  # 오른쪽 맞물림 위치
LEFT_TOOTH  = 6  # 왼쪽 맞물림 위치

for _ in range(k):
    idx_1based, dir_sign = map(int, input().split())
    idx = idx_1based - 1  # 내부는 0-based

    # 1) 전파 방향 계산 (회전은 아직 하지 않음)
    dirs = [0, 0, 0, 0]
    dirs[idx] = dir_sign

    # 왼쪽으로 전파
    for j in range(idx - 1, -1, -1):
        if gears[j][RIGHT_TOOTH] != gears[j + 1][LEFT_TOOTH]:
            dirs[j] = -dirs[j + 1]
        else:
            break

    # 오른쪽으로 전파
    for j in range(idx + 1, 4):
        if gears[j - 1][RIGHT_TOOTH] != gears[j][LEFT_TOOTH]:
            dirs[j] = -dirs[j - 1]
        else:
            break

    # 2) 일괄 회전
    for i in range(4):
        if dirs[i] != 0:
            gears[i].rotate(dirs[i])  # 시계(+1), 반시계(-1)

# 3) 점수 계산: 12시 방향이 S('1')이면 1,2,4,8 가중치
score = 0
for i in range(4):
    if gears[i][0] == '1':
        score += (1 << i)
print(score)