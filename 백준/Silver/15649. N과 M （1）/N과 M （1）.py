# 22 : 30

# N에서 M 만큼의 수열, 중복이 없어야 한다.

N, M = map(int, input().split())

result = []

def backtracking():
    if len(result) == M : # M 만큼 값을 넣었으면, 출력
        print(' '.join(map(str, result)))
    
    for i in range(1, N + 1):
        if i not in result: # i가 안들어있으면, result에 추가 후
            result.append(i)
            backtracking() # backtracking으로 다시 호출을 한다. 
            result.pop()
            
backtracking()