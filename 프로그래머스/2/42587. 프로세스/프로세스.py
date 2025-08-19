# 20 : 00
from collections import deque
# deque을 사용
def solution(priorities, location):
    """
    프린터 큐 시뮬레이션.
    각 원소를 (우선순위, 목표여부)로 큐에 넣고,
    앞의 원소가 뒤쪽보다 낮은 우선순위면 뒤로 보내고,
    아니면 '출력'으로 카운트합니다.
    목표가 출력되는 순간의 카운트를 반환합니다.
    예외: priorities 비어있거나 location 범위 초과 시 -1 반환.
    """
    # --- 입력 검증(데이터 없음/범위 일탈) ---
    if not priorities or not (0 <= location < len(priorities)):
        return -1

    # --- 큐 구성 (priority, is_target) ---
    queue = deque((p, i == location) for i, p in enumerate(priorities))

    printed_count = 0

    while queue:
        cur_priority, is_target = queue.popleft()

        # 뒤에 더 높은 우선순위가 하나라도 있으면 회전
        if any(cur_priority < other_priority for other_priority, _ in queue):
            queue.append((cur_priority, is_target))
            continue

        # 출력 (완료)
        printed_count += 1
        if is_target:
            return printed_count

    # 정상적으로는 도달하지 않음
    return -1