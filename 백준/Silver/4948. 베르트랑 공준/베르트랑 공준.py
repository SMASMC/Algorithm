def is_prime(n):
    arr = [True for i in range(n+1)]
    arr[0] = False
    arr[1] = False

    for i in range(2, n + 1):
        if arr[i] == True:
            j = 2
            while (i * j) <= n:
                arr[i * j] = False
                j += 1
    return arr

result_list = []
while True:
    A = int(input())
    if A == 0:
        break
    result = []

    arr = is_prime(2*A)
    A_arr = is_prime(A)

    result_list.append(arr.count(True) - A_arr.count(True))

for i in result_list:
    print(i)