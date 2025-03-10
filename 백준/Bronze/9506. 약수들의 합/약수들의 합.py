# 9506 약수들의 합 11:15

while True:
    input_num = int(input())
    arr = []
    if input_num == -1:
        break
    else:
        for i in range(1, input_num):
            if input_num % i == 0:
                arr.append(i)
        if sum(arr) == input_num:
            print(input_num,' = ', ' + '.join(str(i) for i in arr),sep='')
        else:
            print(input_num,'is NOT perfect.')