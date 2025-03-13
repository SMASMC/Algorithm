# 2667 단지번호붙이기 21 : 10


def dfs(x,y):
    global count
    if 0<= x < N and 0 <= y < N: # 범위를 벗어나지 않고,
        if board[x][y] == 1:  # 비어 있으면, 셈을 하겠습니다.
            count += 1
            board[x][y] = 0
            dfs(x-1, y) # 상
            dfs(x+1, y)  # 하
            dfs(x, y-1)  # 좌
            dfs(x, y+1)  # 우
    else: # 범위를 벗어났다면 그만두겠습니다.
        return


N = int(input()) # board의 크기

board = [list(map(int, input())) for _ in range(N)] # 단지를 담아내는 board 변수

count = 0 # 각 단지의 아파트 수
count_arr = []# 각 단지의 아파트 수를 모은 배열
for i in range(N):
    for j in range(N):
        if board[i][j] == 1: # 단지가 있으면, 셈을 하겠다.
            count = 0
            dfs(i, j)
            count_arr.append(count) # 아파트를 모두 찾은 count를 배열에 저장하겠습니다.

print(len(count_arr)) # 총 아파트 단지수를 출력
count_arr.sort()
for cnt in count_arr: # 오름차순으로 정렬 뒤, 출력
    print(cnt)