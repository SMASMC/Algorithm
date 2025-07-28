# import sys

# 각 줄을 온점으로 끝내고, 이중 소괄호 대괄호가 짝을 이루는 균형을 이루는 줄이면, yes를 출력,
# 아니라면 no를 출력
while True:
    input_text = input()
    stack_vps = []
    # big_stack_vps = []
    if input_text == '.':
        break
    for row in input_text:
        if row=='.':
            break
        if row == "[" or row == "]":
            if stack_vps and stack_vps[-1] == "[" and row == "]":
                stack_vps.pop()
            else:
                stack_vps.append(row)
        elif row == "(" or row == ")":
            if stack_vps and stack_vps[-1] == "(" and row == ")":
                stack_vps.pop()
            else:
                stack_vps.append(row)
    # for문을 한번 돌고나서
    if not stack_vps: # 스택이 비었다면, yes
        print('yes')
    else:
        print('no')