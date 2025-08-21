def solution(s):
    answer = True
    # 맨 앞에 있는 값이 ) 이거나 맨 뒤 값이 (이면 False
    stack_s = []
    
    for idx_s in s:
        # stack_s가 있고 top이 ( 이고, idx_s가 )이면, stack_s를 pop
        if stack_s and stack_s[-1] == '(' and idx_s == ')':
            stack_s.pop()
        else:
            stack_s.append(idx_s)
    if stack_s:
        answer = False
    return answer