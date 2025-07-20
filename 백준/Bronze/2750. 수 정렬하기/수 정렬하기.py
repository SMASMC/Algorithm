num_len = int(input())

num_arr = []
for i in range(num_len):
    num=int(input())
    num_arr.append(num)

for ni in range(num_len-1):
    for nj in range(ni+1, num_len):
        if num_arr[ni] > num_arr[nj]:
            temp = num_arr[nj]
            num_arr[nj] = num_arr[ni]
            num_arr[ni] = temp

for j in range(num_len):
    print(num_arr[j])