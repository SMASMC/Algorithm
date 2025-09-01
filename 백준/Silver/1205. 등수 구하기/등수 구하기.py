# 15 : 30

# 태수의 새로운 점수가 랭킹 리스트에서 몇등하는지 구하는 프로그램
# 만약 점수가 랭킹 리스트에 올라갈 수 없을 정도라면, -1을 출력
# 만약 랭킹 리스트가 꽉차 있다면, 새 점수가 이전 점수보다 더 좋을 때만 점수를 변경

# N: 두번째줄에 입력될 랭킹 리스트
# new_score: 태수의 새로운 점수
# P: 랭킹 리스트에 올라 갈 수 있는 점수의 개수
N, new_score, P = map(int, input().split())
# 비오름차순으로 되어있는 랭킹 리스트를 입력
current_grade = -1
if N == 0:
    current_grade = 1
else:
    score_list = list(map(int, input().split()))
    score_list.sort(reverse=True)
    if N == P and new_score <= score_list[P-1]:
                    current_grade = -1
    else:
        for n in range(N):
            if score_list[n] <= new_score: # 순위에 든 값보다 크면 현재 n을 순위로
                # 만약 랭킹 리스트가 꽉차있지 않다면, 순위 변동을 실시하겠습니다.
                # 꽉차있지만, 마지막 값보다 크다면,
                    current_grade = n + 1
                    break
        if new_score < score_list[-1]:
            current_grade = N + 1
print(current_grade)