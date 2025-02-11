# 2566번 최댓값

number_arr = [list(map(int, input().split())) for _ in range(9)]
max_number=number_arr[0][0]
max_row = 0
max_col = 0
for row in range(len(number_arr)):
    for col in range(len(number_arr)):
        if max_number <= number_arr[row][col]:
            max_number = number_arr[row][col]
            max_col = col+1
            max_row = row+1
print(max_number)
print(max_row, max_col)