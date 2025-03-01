# 11 : 57

board = [[0]* 100 for _ in range(100)] # 색을 확일할 2차원 배열

T = int(input()) # 색종이 입력 횟수

for _ in range(T):
    x, y = map(int,input().split())
    for xi in range(x,x+10):
        for yi in range(y, y+10):
            board[xi][yi] = 1
count = 0
for row in board:
    count += sum(row)

print(count)