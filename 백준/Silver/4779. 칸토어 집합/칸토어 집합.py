# 4779 칸토어 집합
import sys
input = sys.stdin.readline

def carve(chars, start_idx, segment_len):
    # 길이가 1이면 더 이상 쪼갤 수 없음(기저 조건)
    if segment_len == 1:
        return
    third = segment_len // 3

    # 가운데 1/3 구간을 공백으로 채우기
    mid_start = start_idx + third
    mid_end   = start_idx + 2 * third
    for i in range(mid_start, mid_end):
        chars[i] = ' '  # ← 대입(=) 주의

    # 왼쪽 1/3과 오른쪽 1/3에 대해 재귀
    carve(chars, start_idx, third)
    carve(chars, start_idx + 2 * third, third)

# 입력은 여러 줄(EOF까지)
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    total_len = 3 ** n
    chars = ['-'] * total_len
    carve(chars, 0, total_len)
    print(''.join(chars))
