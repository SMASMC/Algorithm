n=int(input()) # 단어의 개수
group_word_count = 0  # 그룹 단어 개수 저장

for i in range(n):
    word = input()
    seen = set()  # 등장한 문자를 저장할 set
    prev_char = ''  # 이전 문자 저장

    is_group_word = True  # 그룹 단어 여부 확인

    for char in word:
        if char != prev_char:  # 이전 문자와 다를 때만 검사
            if char in seen:  # 이미 등장한 문자라면 그룹 단어가 아님
                is_group_word = False
                break
            seen.add(char)  # 새로운 문자 추가
        prev_char = char  # 현재 문자를 이전 문자로 업데이트
    
    if is_group_word:
        group_word_count += 1  # 그룹 단어 개수 증가

print(group_word_count)  # 그룹 단어 개수 출력
