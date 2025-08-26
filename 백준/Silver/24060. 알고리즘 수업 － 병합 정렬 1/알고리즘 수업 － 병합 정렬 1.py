import sys
from typing import List

sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

def merge(arr: List[int], buf: List[int], left: int, mid: int, right: int,
          kth_target: int, state: dict) -> None:
    """arr[left:right] 병합. tmp→arr 로 복사하는 매 순간 write_count 증가."""
    i, j, t = left, mid + 1, left  # t는 buf에서의 쓰기 시작 인덱스(left에 맞춤)

    # 1) A→buf: 두 구간 병합하여 buf에 정렬 결과 채우기
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            buf[t] = arr[i]; t += 1; i += 1
        else:
            buf[t] = arr[j]; t += 1; j += 1

    while i <= mid:
        buf[t] = arr[i]; t += 1; i += 1
    while j <= right:
        buf[t] = arr[j]; t += 1; j += 1

    # 2) buf→A: 여기서 "쓰기"를 카운트해야 함 (문제의 핵심 포인트)
    for idx in range(left, right + 1):
        arr[idx] = buf[idx]
        state["write_count"] += 1
        if state["write_count"] == kth_target:
            state["kth_value"] = arr[idx]

def merge_sort(arr: List[int], buf: List[int], left: int, right: int,
               kth_target: int, state: dict) -> None:
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, buf, left, mid, kth_target, state)
        merge_sort(arr, buf, mid + 1, right, kth_target, state)
        merge(arr, buf, left, mid, right, kth_target, state)

def main():
    # 입력: N, K / 배열
    line = input().strip()
    if not line:
        # 데이터가 없을 경우: -1 (백준은 출력만 요구하므로 예외 메시지 금지)
        print(-1)
        return
    n, k = map(int, line.split())
    arr = list(map(int, input().split()))

    # 안전성 체크 (제약 위배 시 -1)
    if n <= 0 or not arr or n != len(arr) or not (1 <= k):
        print(-1); return

    buf = [0] * n                  # 공용 임시 버퍼(메모리 낭비 방지)
    state = {"write_count": 0,     # 현재까지 tmp→A 복사 횟수
             "kth_value": -1}      # K번째에 복사된 값(기본 -1)

    merge_sort(arr, buf, 0, n - 1, k, state)
    print(state["kth_value"])

if __name__ == "__main__":
    main()
