# 10773 제로 17 : 30

# 재현이가 잘못된 수를 부를 때마다 0을 외쳐서 해당 스택 인덱스에 0을 넣는다.


# 잘못된 수를 부르면 0을 입력, 0이 입력되면, 마지막 index를 제거한다.
# 재현이가 쓴 값 stack에 있는 값을 sum으로 출력
import sys


# K = int(input())
K = int(sys.stdin.readline().strip()) # 명령의 수 입력
stack = []
for _ in range(K):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))