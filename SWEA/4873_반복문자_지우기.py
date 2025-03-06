# T = int(input())
#
# for tc in range(1, T+1):
#     top = -1
#     S = input()
#     stack_text = [0]*len(S)
#
#     for chr in S:
#         if top >-1 and chr == stack_text[top] : # 스택이 쌓였고, 조회하는 문자가 와 스택 꼭대기와 같으면 해당 스택 줄이기
#             top -=1
#         else: # 꼭대기와 조회하는 문자가 다르면 스택을 쌓겠습니다.
#             top +=1
#             stack_text[top] = chr
#
#     print(f'#{tc} {top + 1}')

# append, pop으로 풀어보자

T = int(input())
for tc in range(1, T+1):
    S = input()

    stack_s = []

    # 현재위치에서 다음위치와 조회를 해서 같으면 pop, 다르면, 현재위치를 다음위치로 바꾸기
    for chr in S:
        if stack_s and chr == stack_s[-1] : # stack이 비어있지 않고, chr 조회하는 값이 stack에 쌓인 마지막 값과 같은 경우
            stack_s.pop()
        else:
            stack_s.append(chr)

    print(f'#{tc} {len(stack_s)}')