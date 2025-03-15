# 1991 트리 순회 21 : 18

def preorder(node):
    if node == '.':
        return
    print(node, end ='') # 현재 노드 출력
    preorder(tree_arr[node][0]) # 왼쪽 자식을 방문합니다.
    preorder(tree_arr[node][1]) # 오른쪽 자식을 방문합니다.

def inorder(node):
    if node == '.':
        return
    inorder(tree_arr[node][0])  # 왼쪽 자식을 방문합니다.
    print(node, end ='') # 현재 노드 출력
    inorder(tree_arr[node][1]) # 오른쪽 자식을 방문합니다.

def postorder(node):
    if node == '.':
        return
    postorder(tree_arr[node][0])  # 왼쪽 자식을 방문합니다.
    postorder(tree_arr[node][1])  # 오른쪽 자식을 방문합니다.
    print(node, end='')  # 현재 노드 출력


N = int(input()) # 노드 수

tree_arr = {} # 노드 수만큼 0으로 초기화
left = [0] * (N+1)
right = [0] * (N+1)

for _ in range(N):
    root, left_n, right_n = input().split()
    if root not in tree_arr.keys(): # 해당 root를 key로 갖고있지 않으면, 넣겠습니다.
        tree_arr[root] = (left_n, right_n)


preorder('A')
print()
inorder('A')
print()
postorder('A')