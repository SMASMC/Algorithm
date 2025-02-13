# 2563번 색종이

paper_count = int(input()) # 색종이 개수

board = [[0]* 100 for _ in range(100)] # 가로 세로 크기가 100인 정사각졍 모양의 도화지
count = 0
for pc in range(paper_count):
    x, y = map(int, input().split())
    for x_row in range(x,x+10):
        for y_col in range(y, y+10):
            if board[x_row][y_col] == 0: # 비어있다면,
                board[x_row][y_col] = 1  # 색을 채우겠다.
                count+=1

print(count)