# 14889 스타트와 링크 - 조합 + 백트래킹
# N명을 두 팀(각 N//2명)으로 나누고, 두 팀의 시너지 차이의 최소값을 찾는다.

n = int(input().strip())  # 전체 인원 N(항상 짝수)
stats = [list(map(int, input().split())) for _ in range(n)]  # 시너지 행렬 S[i][j]
selected = [False] * n    # selected[i]가 True면 팀 A(스타트), False면 팀 B(링크)
min_diff = [1e9] # 파이썬에서 내부 함수에서 갱신하려면 리스트로 감싸 가변 참조 사용

# (선택적 가지치기) 대칭 깨기: 0번을 팀 A에 고정하면 탐색이 절반으로 줄어든다.
selected[0] = True

def evaluate_and_update():
    # 현재 selected 상태로 두 팀의 시너지를 계산하고 min_diff 갱신
    team_a = 0
    team_b = 0
    # S[i][j]와 S[j][i] 모두 더해야 해당 쌍이 됨.
    for i in range(n):
        for j in range(n):
            if selected[i] and selected[j]:
                team_a += stats[i][j]
            elif not selected[i] and not selected[j]:
                team_b += stats[i][j]
    # 절대차를 최소화하는 것이 목표
    diff = abs(team_a - team_b)
    if diff < min_diff[0]:
        min_diff[0] = diff

def dfs(start_idx: int, picked_count: int):

    # start_idx부터 사람들을 순서대로 보며, picked_count명이 팀 A에 뽑히면 평가한다.
    # 팀 A가 N//2명이 되면 팀 구성이 완성 → 평가
    if picked_count == n // 2:
        evaluate_and_update()
        return

    # 남은 인원 수로 N//2명을 채울 수 없으면 가지치기
    remaining = n - start_idx
    need = (n // 2) - picked_count
    if remaining < need:
        return

    # 조합(중복 없이 오름차순)으로 뽑기
    for i in range(start_idx, n):
        if not selected[i]:
            selected[i] = True      # i를 팀 A로 선택
            dfs(i + 1, picked_count + 1)
            selected[i] = False     # 되돌리기(backtrack)

# 0번을 이미 팀 A로 넣었으니, 다음 인덱스 1부터 시작하고 뽑은 수는 1명
dfs(1, 1)

print(min_diff[0])