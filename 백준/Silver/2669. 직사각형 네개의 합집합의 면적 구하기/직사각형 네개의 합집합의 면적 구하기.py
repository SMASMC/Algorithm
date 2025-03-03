# 백준 16 : 32


board = [[0]*100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[x][y] =1

board_sum = 0

for row in board:
    board_sum += row.count(1)

print(board_sum)