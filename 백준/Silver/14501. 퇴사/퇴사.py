# 14501 퇴사 16 : 40
def dfs(day, gold):
    global max_amount
    if day >=N:
        max_amount = max(max_amount, gold)
        return
    if day + day_arr[day] <= N: # 상담을 할 수 있는 경우
        dfs(day + day_arr[day], gold + gold_arr[day])

    dfs(day + 1, gold)

N = int(input()) # 남은 N일
max_amount = 0
day_arr, gold_arr = [], []
for _ in range(N):
    day_input, gold_input = map(int, input().split())
    day_arr.append(day_input)
    gold_arr.append(gold_input) # 입력을 다 받고,

max_amount = 0
dfs(0,0)
print(max_amount)