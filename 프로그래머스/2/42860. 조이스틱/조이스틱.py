# 17 : 00
def solution(name):
    n = len(name)
    
    answer = 0

    # 일단 모두 오른쪽으로만 가는 비용을 기본값으로 둠
    min_horizontal = n - 1
    left_count = 0
    right_count = 0
    for name_chr in name:
        # 13개 이하의 차이면, 그대로 A를 빼놓고 나서의 차이 값을 증가
        if ord(name_chr) - ord('A') <= 13:
            answer += ord(name_chr) - ord('A')
        else: # 13개를 넘어가는 차이라면, 26-A를 빼고 나머지 값을 빼면 된다.
            answer += 26 - (ord(name_chr) - ord('A'))
            
    for i in range(n):
        # i 이후 연속된 'A' 구간의 끝을 찾는다
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        # 전략 1) 오른쪽으로 i칸 갔다가 되돌아와서 끝까지 가기
        move_right_then_left = 2 * i + (n - next_idx)

        # 전략 2) 오른쪽으로 i칸 간 뒤, 남은 끝쪽 먼저 갔다가 되돌아오기
        move_left_then_right = i + 2 * (n - next_idx)

        # 두 전략 중 더 작은 것과 현재 최소값 비교
        min_horizontal = min(min_horizontal, move_right_then_left, move_left_then_right)
    # 좌우 이동 최소값을 answer에 더하기
    answer += min_horizontal

    return answer

'''
    # A~Z까지의 순서 및 크기를 변환 시켜주는 프로그램
    # 각 문자들의 자리들이 A부터 시작해서 name의 문자들에 맞춰서 변환시켜줘야함.
    # 그런데, 뒤로 이전시켜서 나오는 값이 더 효율적이면 이전알파벳으로하는 것을 적용해야한다.
    # 26개의 알파벳
    answer = 0
    left_count = 0
    right_count = 0
    for name_chr in name:
        # 13개 이하의 차이면, 그대로 A를 빼놓고 나서의 차이 값을 증가
        if ord(name_chr) - ord('A') <= 13:
            answer += ord(name_chr) - ord('A')
        else: # 13개를 넘어가는 차이라면, 26-A를 빼고 나머지 값을 빼면 된다.
            answer += 26 - ord(name_chr) - ord('A')
    # 각 위치에 따른 ord차이 값을 저장. 그 뒤, 오른쪽 왼쪽 이동 값에 따라서 값을 따로 구하고,
    # 비교 후, 작은 값을 answer에 추가
    # name: 목표 문자열

'''