board = [list(input()) for _ in range(5)]

new_word=''
max_idx=max(len(board[row]) for row in range(5)) # 가장 많은 index => col을 지닌 값을 찾기

for col in range(max_idx):
    for row in range(5):
        if col < len(board[row]): # 최대 크기를 벗어나지 않는다면.
            new_word +=board[row][col]

print(new_word)