x, y = map(int, input().split())  # 가로(x), 세로(y)
N = int(input())  # 상점 개수

board = []  # 상점들의 위치를 저장할 리스트
for _ in range(N + 1):
    board.append(list(map(int, input().split())))  # 상점 및 동근이 위치 저장

dong_dir, dong_pos = board[-1]  # 동근이의 위치 정보
min_path_sum = 0

for i in range(N):
    store_dir, store_pos = board[i]  # 상점의 방향과 위치

    if dong_dir == store_dir:  # 같은 방향에 위치한 경우
        min_path_sum += abs(dong_pos - store_pos)

    elif dong_dir in [1, 2] and store_dir in [1, 2]:  # 북쪽 & 남쪽에 위치한 경우
        clockwise_dist = dong_pos + store_pos + y  # 시계 방향 거리
        counter_clockwise_dist = (x - dong_pos) + (x - store_pos) + y  # 반시계 방향 거리
        min_path_sum += min(clockwise_dist, counter_clockwise_dist)

    elif dong_dir in [3, 4] and store_dir in [3, 4]:  # 서쪽 & 동쪽에 위치한 경우
        clockwise_dist = dong_pos + store_pos + x  # 시계 방향 거리
        counter_clockwise_dist = (y - dong_pos) + (y - store_pos) + x  # 반시계 방향 거리
        min_path_sum += min(clockwise_dist, counter_clockwise_dist)

    else:  # 서로 반대편에 위치한 경우 (북-남, 동-서)
        if dong_dir == 1:  # 북쪽
            if store_dir == 3:
                min_path_sum += dong_pos + store_pos
            else:
                min_path_sum += (x - dong_pos) + store_pos
        elif dong_dir == 2:  # 남쪽
            if store_dir == 3:
                min_path_sum += dong_pos + (y - store_pos)
            else:
                min_path_sum += (x - dong_pos) + (y - store_pos)
        elif dong_dir == 3:  # 서쪽
            if store_dir == 1:
                min_path_sum += dong_pos + store_pos
            else:
                min_path_sum += (y - dong_pos) + store_pos
        elif dong_dir == 4:  # 동쪽
            if store_dir == 1:
                min_path_sum += dong_pos + (x - store_pos)
            else:
                min_path_sum += (y - dong_pos) + (x - store_pos)

print(min_path_sum)