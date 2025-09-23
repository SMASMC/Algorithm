# 2110 공유기 설치 22: 20 
import sys 

input = sys.stdin.readline
N, C = map(int, input().split())

list = []

for _ in range(N):
    list.append(int(input()))
list.sort()

start = 1 # 굥유기 최소 거리
end = list[-1] - list[0] # 공유기 거리 최대
result = 0

while (start <= end):
    mid = (start + end) // 2 # 현재 공유기 거리
    current = list[0]
    count = 1

    # 공유기 설치 몇 대 할 수 있는지 체크
    for i in range(1, len(list)):
        if list[i] >= current + mid:
            count += 1
            current = list[i]
    # 공유기 설치 수가 목표 보다 크면 공유기 사이 거리 늘림
    if count >= C:
        start = mid + 1
        result = mid
    # 공유기 설치 수가 목표 보다 작으면 공유기 사이 거리 줄임
    else:
        end = mid - 1
print(result)