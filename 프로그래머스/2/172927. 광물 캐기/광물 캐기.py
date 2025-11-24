# 최소 피로도 소모를 반환하는 함수 만들기
# diamond=1, iron=1, rock=1
# 동일하면 1, 다철은 5, 다돌은 25, 돌철은 5
# picks가 곡괭이, minerals가 광물
def solution(picks, minerals):
    # 예외 처리: 곡괭이 없거나 광물 없으면 피로도는 0
    if not picks or sum(picks) == 0 or not minerals:
        return 0

    total_picks = sum(picks)              # 곡괭이 총 개수
    max_minerals = total_picks * 5        # 캘 수 있는 최대 광물 수
    limit = min(len(minerals), max_minerals)
    usable_minerals = minerals[:limit]    # 실제로 캘 수 있는 광물만 사용

    groups = []  # 각 원소: (돌곡괭이 피로도, dia개수, iron개수, stone개수)

    # 1. 광물을 5개씩 그룹으로 나누어서, 그룹 난이도 계산
    for i in range(0, limit, 5):
        chunk = usable_minerals[i:i+5]

        dia = iron = stone = 0  # 불필요한 재선언 없이 한 번에 초기화
        for m in chunk:
            if m == "diamond":
                dia += 1
            elif m == "iron":
                iron += 1
            else:  # "stone"
                stone += 1

        # 돌 곡괭이로 캤을 때 피로도 (그룹 난이도 지표)
        stone_cost = dia * 25 + iron * 5 + stone
        groups.append((stone_cost, dia, iron, stone))

    # 2. 돌 곡괭이로 캤을 때 피로도가 큰 순서대로 정렬 → 어려운 그룹부터 좋은 곡괭이 배치
    groups.sort(reverse=True)

    answer = 0
    group_idx = 0  # 현재 처리 중인 그룹 인덱스

    # 3. 곡괭이를 좋은 것(dia)부터 차례대로 그룹에 배정
    for pick_type, count in enumerate(picks):  # 0: dia, 1: iron, 2: stone
        for _ in range(count):
            if group_idx >= len(groups):       # 더 이상 캐야 할 그룹이 없으면 종료
                return answer

            _, dia, iron, stone = groups[group_idx]

            if pick_type == 0:          # 다이아 곡괭이
                answer += dia + iron + stone
            elif pick_type == 1:        # 철 곡괭이
                answer += dia * 5 + iron + stone
            else:                       # 돌 곡괭이
                answer += dia * 25 + iron * 5 + stone

            group_idx += 1

    return answer