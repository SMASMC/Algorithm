# N은 숫자들의 개수, M은 3장의 합에 가까운지 확인
N, M = map(int, input().split())

num_list = list(map(int, input().split()))
most_sum = 0

for i in range(len(num_list)-2):
    for j in range(i+1, len(num_list)-1):
        for z in range(j+1, len(num_list)):
            cur_sum = 0
            cur_sum += num_list[i]+num_list[j]+num_list[z]
            if (most_sum < cur_sum) and (cur_sum <= M):
                most_sum = cur_sum

print(most_sum)