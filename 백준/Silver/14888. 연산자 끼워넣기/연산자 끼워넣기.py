# 14888 연산자 끼워 넣기 19 : 50

N = int(input()) # 수의 개수
num_list = list(map(int, input().split())) # N만큼의 수의 list
add, sub, mul, div = map(int, input().split()) # 각 사칙연산자의 개수

min_x = 1e9 # 최소값을 위해 10억 할당
max_x = -1e9 # 최대값을 위해 -10억 할당

def dfs(depth, total, add, sub, mul, div):
    global min_x, max_x
    if depth == N: # 모든 사칙연산을 배치한 경우
        min_x = min(total, min_x) # 최대값
        max_x = max(total, max_x) # 최소값
        return
    # depth != N 인 경우에 연산을 마무리 짓지 않았으므로 재귀
    # 각 위치에 맞게 연산한 경우 연산을 진행했으므로, 해당되는 연산을 -1시켜준다.
    if add:
        dfs(depth+1, total + num_list[depth], add-1, sub, mul, div)
    if sub:
        dfs(depth+1, total - num_list[depth], add, sub-1, mul, div)
    if mul:
        dfs(depth+1, total * num_list[depth], add, sub, mul-1, div)
    if div: # 소수점이 발생하지 않도록 나누셈 진행
        dfs(depth+1, int(total / num_list[depth]), add, sub, mul, div-1)

dfs(1, num_list[0], add, sub, mul, div)
print(max_x) # 최댓 값
print(min_x) # 최소 값