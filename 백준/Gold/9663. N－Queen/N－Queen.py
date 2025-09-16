import sys

data = sys.stdin.read().strip().split()
if not data:                 # 데이터 없음 방어
    print(0)

n = int(data[0])
if n <= 0:                   # 비정상 입력 방어
    print(0)

sys.setrecursionlimit(1_000_000)

all_mask = (1 << n) - 1      # n비트가 1인 마스크 (모든 열 사용 가능)
answer_count = 0

def dfs(used_cols: int, used_diag_l: int, used_diag_r: int):
    global answer_count
    # 모든 열이 채워졌다면(= n개의 퀸 배치 완료) 경우의 수 +1
    if used_cols == all_mask:
        answer_count += 1
        return

    # 이번 행에서 놓을 수 있는 위치들(비트 집합)
    # 아직 쓰지 않은 열/대각선만 남김
    available = all_mask & ~(used_cols | used_diag_l | used_diag_r)

    # 가능한 위치를 하나씩 뽑아 시도 (p = 최하위 1비트)
    while available:
        p = available & -available      # 최하위 set bit
        available -= p                  # 해당 자리 소거

        # 다음 행으로 내려갈 때 대각선 상태는 시프트
        # '\' 대각선은 왼쪽으로 한 칸 이동 → << 1, 범위 초과 비트는 마스크로 제거
        # '/' 대각선은 오른쪽으로 한 칸 이동 → >> 1
        dfs(
            used_cols | p,
            (used_diag_l | p) << 1 & all_mask,
            (used_diag_r | p) >> 1
        )

dfs(0, 0, 0)
print(answer_count)