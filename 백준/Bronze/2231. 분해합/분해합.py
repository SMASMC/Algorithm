n = int(input())

for i in range(1, n+1):
    num = sum((map(int, str(i))))  # i의 각 자릿수를 더함
    num_sum = i + num  # 분해합 = 생성자 + 각 자릿수의 합
    if num_sum == n:
        print(i)
        break
    if i == n:  # 생성자 i와 입력값이 같다는 건, 생성자가 없음
        print(0)