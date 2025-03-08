# 10일차 - 비밀번호 # 21 : 10

T = 10
for tc in range(1, T+1):
    top = -1 # 스택에 가장 위에있는 값을 찾기위한 선언
    N, chr_s = input().split() # 문자열의 길이, 문자열
    N = int(N) # chr_s의 문자열 길이를 정수형으로 변환
    stack_s = []
    print(len(chr_s))
    for i in range(N):
        if top > -1 and stack_s[-1] == chr_s[i]: # stack_s의 마지막 요소와 chr_s의 현재 요소가 같으면,
            top -= 1 # 뒤로 한칸 미루겠습니다.
            stack_s.pop()
        else:
            top +=1
            stack_s.append(chr_s[i])

    print(f'#{tc}', end=' ')
    for s in stack_s:
        print(s, end='')
    print()