# 11725 트리의 부모 찾기 20 : 51
import sys
sys.setrecursionlimit(10**6) # 재귀 깊이를 충분히 늘림 => 런타임 에러 발생 안하도록 선언
def find_parent_dfs(node):
    for child in tree[node]:
        if parent_arr[child] == 0:  # 방문하지 않은 자식 노드만 탐색
            parent_arr[child] = node  # 부모 저장
            find_parent_dfs(child)  # 재귀적으로 탐색

N = int(input())  # 노드 개수

arr = []  # 입력 데이터를 저장할 리스트
tree = [[] for _ in range(N+1)]  # 인접 리스트 (0번 인덱스 사용 안함)
parent_arr = [0] * (N+1)  # 부모 정보 저장 배열

# 간선 정보 입력 및 저장
for _ in range(N-1):
    a, b = map(int, input().split())
    arr.extend([a, b])  # 기존 코드 유지
    tree[a].append(b)  # 양방향 연결
    tree[b].append(a)

# 루트 노드는 1번 (문제에서 명시)
parent_arr[1] = -1  # 루트 노드의 부모는 없음을 의미 (-1)
find_parent_dfs(1)  # DFS 탐색 시작

# 2번 노드부터 N번 노드까지 부모 출력
for i in range(2, N+1):
    print(parent_arr[i])
