# from collections import deque
def solution(prices):
    answer = []
    # [1,2,3,2,3] 에서 prices[0]인 1은 끝까지 안떨어짐
    # 가격이 증가 혹은 유지가 되면 1초씩 증가, 떨어지면 증가 안함.
    # prices = deque(prices)
    for i in range(len(prices)):
        count = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
    return answer