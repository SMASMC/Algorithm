# 파스칼의 삼각형 15 : 40

T = int(input()) # 테스트 케이스


for tc in range(1, T+1):
    N = int(input()) # 파스칼 삼각형의 크기
    stack_n = []
    stack_n.append([1])

    for n in range(1,N):
        row = [1]
        for j in range(1, n):
            row.append(stack_n[n-1][j-1] + stack_n[n-1][j]) # 왼쪽 위 + 오른쪽 위
        row.append(1)
        stack_n.append(row)
    print(f'#{tc}')
    for row in stack_n:
        print(*row)