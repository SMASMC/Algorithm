def solution(numbers, target):
    # 타겟 넘버 - DFS(백트래킹) + 가지치기
    # - numbers: 1..50의 자연수, 길이 2..20
    # - target: 1..1000
    # 반환: +/−로 조합해 target을 만드는 방법 수
    n = len(numbers)

    # 남은 원소들의 합(접미 합) 미리 계산 -> O(1)로 remain 구함
    suffix_sum = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + numbers[i]

    # DFS 재귀 깊이 최대 20
    def dfs(idx: int, cur_sum: int) -> int:
        # 가지치기 => 남은 합으로도 target에 도달 불가하면 중단
        remain = suffix_sum[idx]
        if abs(target - cur_sum) > remain:
            return 0

        if idx == n:  # 모든 숫자 사용
            return 1 if cur_sum == target else 0

        # 현재 숫자를 + 혹은 - 로 선택
        plus  = dfs(idx + 1, cur_sum + numbers[idx])
        minus = dfs(idx + 1, cur_sum - numbers[idx])
        answer = plus + minus
        return answer

    return dfs(0, 0)
