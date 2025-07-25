from collections import deque
import sys

T = int(sys.stdin.readline())  # 더 빠른 입력 처리

queue_x = deque()

for _ in range(T):
    input_command = sys.stdin.readline().strip().split()
    command = input_command[0]

    if command == 'push':
        X = int(input_command[1])
        queue_x.append(X)
    elif command == 'pop':
        print(queue_x.popleft() if queue_x else -1)
    elif command == 'front':
        print(queue_x[0] if queue_x else -1)
    elif command == 'back':
        print(queue_x[-1] if queue_x else -1)
    elif command == 'size':
        print(len(queue_x))
    elif command == 'empty':
        print(0 if queue_x else 1)
