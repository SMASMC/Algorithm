# 15650 N과 M (2)

# 조합(오름차순) 출력: 1..n 중 m개 선택
# 핵심 아이디어: 시작 인덱스를 앞으로만 밀며 DFS → 자동으로 오름차순/중복 방지

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
path = []                 # 현재 선택된 수열 (길이 ≤ m)
out_lines = []            # 출력 버퍼 (한 번에 출력; print 남발 방지)

def dfs(start: int, picked: int) -> None:
    # 목표 길이에 도달하면 출력 버퍼에 저장
    if picked == m:
        out_lines.append(" ".join(map(str, path)))
        return

    # 남은 칸을 채울 수 있을 만큼만 루프(불필요한 반복 방지)
    # 마지막으로 뽑을 수 있는 시작값 상한: n - (m - picked) + 1
    limit = n - (m - picked) + 1
    for num in range(start, limit + 1):
        path.append(num)           # 선택
        dfs(num + 1, picked + 1)   # 다음 숫자는 현재보다 큰 수부터
        path.pop()                 # 되돌리기

dfs(1, 0)
sys.stdout.write("\n".join(out_lines))