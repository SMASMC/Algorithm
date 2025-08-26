# 15 : 24
# 파란색으로 선택된 행을 표기
# 한번에 한 행만 선택
# n : 행의 개수
# k : 처음에 선택된 행의 위치
# U X : 현재 선택된 행에서 X칸 위에 있는 행을 선택 (만약 범위를 벗어난다면, 현재 위치에 그대로있는다.)
# D X : 현재 선택된 행에서 X칸 아래에 있는 행을 선택(만약 범위를 벗어난다면, 현재 위치에 그대로있는다.)
# C : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택 if 마지막 행이 삭제된 경우 바로 윗 행을 선택
# Z : 가장 최근에 삭제된 행을 원래대로 복구, 하지만 현재 선택된 행을 바뀌지 않는다
# 행 번호를 다시 이전으로 돌려야한다
from typing import List, Tuple

def solution(n: int, k: int, cmd: List[str]) -> str:
    """
    표 편집 - 연결 리스트 + 삭제 스택
    규칙 확장: U/D 시 범위를 벗어나면 '원위치' (이동 무효)
    반환: 각 행의 상태를 'O'(존재)/'X'(삭제) 문자열로 반환
    """

    # --- 예외 처리(데이터 없음/범위 문제) ---
    if n <= 0:
        return ""
    if not (0 <= k < n):
        # k가 비정상이면 0으로 보정 (혹은 raise ValueError)
        k = max(0, min(k, n - 1))
    if not cmd:
        return "O" * n

    # --- 이중 연결 리스트(배열로 구현) ---
    prev_idx = [-1] + [i for i in range(n - 1)]      # prev_idx[i] = i-1, 0은 -1
    next_idx = [i + 1 for i in range(n - 1)] + [-1]  # next_idx[i] = i+1, n-1은 -1
    cur = k

    # --- 삭제 스택: (행, prev, next) ---
    deleted_stack: List[Tuple[int, int, int]] = []

    # --- 유틸: 위/아래 이동 (범위 벗어나면 원위치) ---
    def move_up(steps: int) -> None:
        nonlocal cur
        origin = cur
        moved = 0
        while moved < steps and prev_idx[cur] != -1:
            cur = prev_idx[cur]
            moved += 1
        if moved < steps:  # 끝 도달 → 이동 무효
            cur = origin

    def move_down(steps: int) -> None:
        nonlocal cur
        origin = cur
        moved = 0
        while moved < steps and next_idx[cur] != -1:
            cur = next_idx[cur]
            moved += 1
        if moved < steps:  # 끝 도달 → 이동 무효
            cur = origin

    # --- 명령 처리 ---
    for raw in cmd:
        c = raw[0]
        if c == 'U' or c == 'D':
            # "U X" / "D X": 문자열 → 정수 변환 필수
            _, s = raw.split()
            steps = int(s)
            if c == 'U':
                move_up(steps)
            else:
                move_down(steps)

        elif c == 'C':
            # 현재 행 삭제 → 스택에 (행, prev, next) 저장
            p, n_ = prev_idx[cur], next_idx[cur]
            deleted_stack.append((cur, p, n_))

            # 양쪽 연결 재구성
            if p != -1:
                next_idx[p] = n_
            if n_ != -1:
                prev_idx[n_] = p

            # 다음 선택: 아래가 있으면 아래, 아니면 위
            cur = n_ if n_ != -1 else p

        elif c == 'Z':
            # 최근 삭제 복구 (현재 선택 cur은 변하지 않음)
            if not deleted_stack:
                continue  # 복구할 것이 없음
            i, p, n_ = deleted_stack.pop()

            if p != -1:
                next_idx[p] = i
            if n_ != -1:
                prev_idx[n_] = i
            prev_idx[i], next_idx[i] = p, n_

    # --- 결과 구성: 살아있는 행은 'O', 스택에 남은 삭제 행은 'X' ---
    result = ['O'] * n
    for i, _, _ in deleted_stack:
        result[i] = 'X'
    return "".join(result)
