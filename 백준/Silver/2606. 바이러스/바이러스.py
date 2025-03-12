def dfs(v):
    stack = [v]  # 시작 노드를 스택에 삽입
    visited[v] = 1  # 시작 노드를 방문 처리
    count = 0  # 감염된 컴퓨터 수

    while stack:
        node = stack.pop()
        for neighbor in cp_graph[node]:  # 현재 노드에 연결된 모든 컴퓨터 탐색
            if not visited[neighbor]:  # 방문하지 않았다면 감염 처리
                visited[neighbor] = 1
                stack.append(neighbor)
                count += 1  # 감염된 컴퓨터 수 증가

    return count


# 입력 처리
cp_cnt = int(input())  # 컴퓨터 개수
cp_connect_cnt = int(input())  # 직접 연결된 쌍 개수

cp_graph = [[] for _ in range(cp_cnt + 1)]  # 1번부터 시작하는 노드이므로 +1 크기로 생성
visited = [0] * (cp_cnt + 1)  # 방문 여부 체크 리스트

# 그래프 생성 (양방향)
for _ in range(cp_connect_cnt):  
    num1, num2 = map(int, input().split())
    cp_graph[num1].append(num2)
    cp_graph[num2].append(num1)

# DFS 실행 및 결과 출력
infected_computers = dfs(1)
print(infected_computers)
