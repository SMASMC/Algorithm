# 2805 나무 자르기 21: 27
import sys

input = sys.stdin.readline
# 1 번째 방법 시간 초과
# N, M = map(int, input().split()) # N: 나무의 수, M: 집에가져가기 위한 잘라진 나무의 길이

# tree_list = list(map(int, input().split()))
# tree_len = min(tree_list) # 나무의 최대 높이
# # 완전탐색으로 1~inf까지 값이 이상인 나머지 값을 잘라내서 저장시킨다음 그 값이 M이면 정답인걸로
# while True:
#     cur_len = 0 # 잘라진 나무의 길이
#     for i in range(N):
#         if tree_list[i] > tree_len:
#             sub = tree_list[i] - tree_len
#             cur_len += sub
#     if cur_len == M:
#         print(tree_len)
#         break
#     tree_len += 1
# --------------------
# 2 번째 방법
N, M = map(int, input().split()) # N: 나무의 수, M: 집에가져가기 위한 잘라진 나무의 길이
tree_list = list(map(int, input().split()))
max_len = max(tree_list)
low = 0
high = max_len
answer = 0

while low <= high:
    middle = (low + high) // 2 # 시도 높이
    cur_len = 0
    for tree in tree_list:
        if tree > middle:
            cur_len += (tree - middle)
        if cur_len >= M:
            break
    if cur_len >= M:
        answer = middle
        low = middle + 1
    else: # 높이 낮추기
        high = middle -1
print(answer)