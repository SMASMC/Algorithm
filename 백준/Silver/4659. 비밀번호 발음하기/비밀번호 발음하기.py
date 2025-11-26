# 4659 비밀번호 발음하기
import sys

input = sys.stdin.readline

input_word=''
vowels='aeiou'
while True:
    input_word = input().strip()
    if input_word == 'end':
        break
    is_acceptable = True
    has_vowel = False # 모음을 지니는지 확인하는 변수
    vowel_cnt = 0 # 모음 개수
    cons_cnt = 0 # 자음 개수
    prev_chr = '' # 이전 글자를 저장해서 e 또는 o 인지 파악
    for word in input_word:
        if word in vowels:
            has_vowel = True
            vowel_cnt += 1
            cons_cnt = 0
        else:
            cons_cnt += 1
            vowel_cnt = 0
        if vowel_cnt >=3 or cons_cnt >=3:
            is_acceptable = False
            break
        if prev_chr == word and word not in ['e', 'o']:
            is_acceptable = False
            break
        prev_chr = word
        
    if not has_vowel:
        is_acceptable = False
    print(f'<{input_word}> is {"acceptable" if is_acceptable else "not acceptable"}.')