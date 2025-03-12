import sys

N = int(sys.stdin.readline().strip())  # 명령의 수 입력
stack = []  # 스택 선언

for _ in range(N):
    order = sys.stdin.readline().strip().split()

    if order[0] == '1':  # "1 X": X를 스택에 push
        stack.append(int(order[1]))

    elif order[0] == '2':  # "2": pop() 후 출력
        print(stack.pop() if stack else -1)

    elif order[0] == '3':  # "3": 스택 크기 출력
        print(len(stack))

    elif order[0] == '4':  # "4": 스택이 비어있는지 확인 (1이면 비어있음)
        print(1 if not stack else 0)

    elif order[0] == '5':  # "5": 스택의 top 출력
        print(stack[-1] if stack else -1)
