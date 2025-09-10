# 00: 09 간토어 집합

import sys

input = sys.stdin.readline

def cantor(chars, start_idx, segment):
    if segment == 1:
        return # 1이면, 중단하겠습니다.
    third=segment // 3
    mid_start = start_idx + third
    mid_end = start_idx + 2*third
    chars[mid_start: mid_end] = ' ' * (mid_end - mid_start) # 가운데를 빈공간으로 저장
    cantor(chars, start_idx, third) # 왼쪽에 빈공간 저장
    cantor(chars, start_idx + 2*third, third) # 오른쪽에 빈공간 저장

# 파일의 끝에서 입력을 멈춤. => EOF인데, try, except로 예외처리하면 됨.
while True:
    try:
        N = int(input())
        total_length = 3**N
        chars = ['-']*total_length
        cantor(chars, 0, total_length)
        print(''.join(chars))
    except:
        break