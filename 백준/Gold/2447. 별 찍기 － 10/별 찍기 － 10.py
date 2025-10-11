# 23: 00 별 찍기 - 10 / 2447번

N = int(input())

init = ['***', '* *', '***'] # N이 3인경우

def recursion(n = 3, arr = init):

    if n == N: # N이 3이면 바로 출력
        return arr

    tmp = []

    for i in range(n): # 공백없는 구간
        tmp.append(arr[i] * 3)

    for i in range(n): # 공백있는 구간
        tmp.append(arr[i] + ' ' * n + arr[i])

    for i in range(n): # 공백없는 구간
        tmp.append(arr[i] * 3)

    return recursion(n * 3, tmp)

answer = recursion(3, init)

for line in answer:
    print(line)