# 16173 점프왕 쩰리(Small) 15 : 10


def dfs(i, j):
    if visited[i][j]:# 이미 방문한 곳이면 탐색을 중단합니다.
        return
    visited[i][j] = True

    global board
    global is_fail
    jump_len = board[i][j]
    if i == N-1 and j == N-1:
        is_fail = True
        print('HaruHaru')
        return
    if i + jump_len < N : # 오른쪽이든, 아래쪽이든 넘지 않으면 된다.
        dfs(i + jump_len, j)
    if j + jump_len < N :
        dfs(i, j+jump_len)

N = int(input())
is_fail = False
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
dfs(0, 0) # board의 크기와 board에서 이동할 거리의 크기를 전달
if is_fail == False:
    print('Hing')