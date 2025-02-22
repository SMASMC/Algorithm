N = int(input()) # 색종이의 수

board = [[0] * 1001 for _ in range(1001)]

for n in range(1, N+1):
    x1, y1, width, height = map(int,input().split()) # 색종이의 좌표 및 크기
    x2, y2 = x1 + width, y1 + height # 색종이의 범위는 가로, 세로의 길이를 더 추가야해한다.
    for nx in range(x1, x2):
        for ny in range(y1, y2):
            board[nx][ny] = n

for num in range(1, N+1): # 색종이의 범위를 읽어서 count 후 출력한다.
    count = sum(row.count(num) for row in board)
    print(count)