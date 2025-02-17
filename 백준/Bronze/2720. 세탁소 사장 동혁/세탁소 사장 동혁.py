# 거스름돈은 항상 $5 이하이고, 동전의 개수를 최소화하여 주려고한다.
# 제일 큰수로 먼저 나누고, 나머지로 다음으로 큰 수로 나누고를 반복하여 나머지를 0으로 만드는 프로그램

def greedy_money(amount):
    greedy_money = [25, 10, 5, 1]
    arr =[]

    for i in greedy_money:
        arr.append(amount // i)
        amount = amount%i

    return arr

T = int(input()) # 테스트 케이스 

for tc in range(1, T+1):
    amount = int(input())

    print(*greedy_money(amount))