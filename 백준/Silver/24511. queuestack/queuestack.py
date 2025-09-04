# 24511 queuestack 19:46

# N-1에 위치에 값을 넣고, N 위치에 있던 값을 빼낸다.
import sys
from collections import deque
input_text = sys.stdin.readline
N = int(input_text()) # 자료구조의 개수
A = list(map(int, input_text().split())) # 수열 A
B = list(map(int, input_text().split())) # 수열 B 초기 상태
M = int(input_text()) # 삽입할 수열의 길이 M
C = list(map(int, input_text().split())) # 삽일할 수열


# que로 deque에 순서대로 쌓아두고,
# 수열 C에 들어오는대로 맨앞에 쌓고, 맨뒤에 있는 값을 뽑아낸다.
D = deque([]) # deque로 값을 저장
answer = []
for n in range(N):
    if A[n] == 0: # queue이다. 값을 D에 빼놓자
        D.append(B[n])
for m in range(M):
    D.appendleft(C[m])
    answer.append(D.pop())
for a in answer:
    print(a, end=' ')