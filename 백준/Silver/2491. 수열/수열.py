N = int(input())  # 입력되는 수들의 길이
num_arr = list(map(int, input().split()))

if N == 1:
    print(1)
    exit()

max_continue_length = 1  # 최소 연속 길이는 1
increase_count = 1  # 증가하는 수열 길이
decrease_count = 1  # 감소하는 수열 길이

for i in range(1, N):
    if num_arr[i] >= num_arr[i - 1]:  # 증가하는 경우
        increase_count += 1
    else:
        increase_count = 1  # 증가 수열 끊김

    if num_arr[i] <= num_arr[i - 1]:  # 감소하는 경우
        decrease_count += 1
    else:
        decrease_count = 1  # 감소 수열 끊김

    max_continue_length = max(max_continue_length, increase_count, decrease_count)

print(max_continue_length)
