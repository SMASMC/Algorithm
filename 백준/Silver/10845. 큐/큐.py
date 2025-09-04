# 10845 큐 19 : 11
import sys
from collections import deque
input_text = sys.stdin.readline
N = int(input_text()) # 명령의 수

num_list = deque([])

for _ in range(N):
    read = input_text().split()
    command = read[0]
    if command == 'push':
        num_list.append(int(read[1]))
    elif command == 'pop':
        if len(num_list) == 0:
            print('-1')
        else:
            print(num_list.popleft())
    elif command == 'size':
        print(len(num_list))
    elif command == 'empty':
        if len(num_list) == 0:
            print('1')
        else:
            print('0')
    elif command == 'front':
        if len(num_list) != 0:
            print(num_list[0])
        else:
            print('-1')
    elif command == 'back':
        if len(num_list) != 0:
            print(num_list[-1])
        else:
            print('-1')