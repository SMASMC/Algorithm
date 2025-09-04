# 9655 돌 게임
import sys
input = sys.stdin.readline

N = int(input().strip()) # 돌의 개수

# 상근이와 창영이는 턴을 번갈아가면서 돌을 가져간다.
# 돌은 1 or 3 개를 가져간다.
# 마지막에 돌을 가져가는 사람이 게임을 이기게 됨.
# 상근이가 이기면 SK 아니면 CY
# 상근이 먼저 돌을 가져간다.
# ex) 5
# 1, 3, 5
# 1~3, 5
# 1, 5
# ex) 4
# 1, 3 창영 승
# 1~3 창영 승
winner = 'SK'
if N %2 == 0: # 짝수인 경우에는 창영 승
    winner = 'CY'
print(winner)