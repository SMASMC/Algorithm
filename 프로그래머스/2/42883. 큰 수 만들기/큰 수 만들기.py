def solution(number, k):
    # number 숫자 문자열 (길이 2 ~ 1_000_000)
    # k 제거할 자릿수 (1 ~ len(number)-1)
    # 반환: k개 제거 후 만들 수 있는 '가장 큰 숫자' 문자열
    n = len(number)
    if not (1 <= k < n):           # 제약 위반 시, 합리적 반환
        # k == 0이면 원문 그대로가 최댓값
        return number if k == 0 and n >= 1 else ""

    # 모노톤 스택 (내림차순 유지)
    remain_to_remove = k
    stack_digits: List[str] = []
    push = stack_digits.append
    pop = stack_digits.pop

    for digit_char in number:
        # 현재 숫자가 직전 숫자보다 크면, 자릿값 높은 쪽을 살리기 위해 pop
        while remain_to_remove and stack_digits and stack_digits[-1] < digit_char:
            pop()
            remain_to_remove -= 1
        push(digit_char)

    # 아직 제거해야 할 개수가 남았다면(대부분 뒤에서 제거)
    if remain_to_remove:
        # 뒤에서 남은 개수만큼 자르기 (스택 길이는 n, remain_to_remove ≤ n-1이므로 안전)
        stack_digits = stack_digits[:-remain_to_remove]

    # 최종 결과 문자열
    result_str = "".join(stack_digits)
    return result_str
