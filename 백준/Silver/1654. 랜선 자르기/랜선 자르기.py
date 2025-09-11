# 1654 랜선 자르기 19: 20

import sys

input = sys.stdin.readline

K, N = map(int, input().split())
# K: 소지하고 있는 랜선의 개수
# N: 필요한 랜선의 개수
# K줄에 걸쳐 소지하고 있는 랜선들의 길이를 각각 입력한다.
# N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력
lan_line = []
for _ in range(K):
    lan_line.append(int(input()))
lan_line.sort() # 정렬
low = 1
high = max(lan_line)
mid = (low + high) // 2
k_count = 0
while low <= high:
    mid = (low + high) // 2  # 이번에 시험해 볼 자르는 길이
    pieces_count = 0

    # mid 길이로 잘랐을 때 만들 수 있는 조각 수 계산
    for length in lan_line:
        pieces_count += length // mid
        if pieces_count >= N:  # 이미 충분하면 조기 종료(미세 최적화)
            break

    if pieces_count >= N:
        # mid 길이는 가능 → 더 긴 길이도 가능한지 오른쪽으로 이동
        best_length = mid
        low = mid + 1
    else:
        # mid 길이는 불가능 → 더 짧게
        high = mid - 1

print(best_length)
