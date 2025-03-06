# 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램

def pre_order(n):
    global cnt
    if n:  # 존재하는 정점이면
        cnt += 1
        pre_order(ch1[n])
        pre_order(ch2[n])


def pre_order2(n):
    if n == 0:  # 존재하지 않는 정점이면
        return 0
    else:
        l = pre_order2(ch1[n])  # 왼쪽 서브트리의 정점 수
        r = pre_order2(ch2[n])  # 오른쪽 서브트리의 정점 수
        return l + r + 1  # 자기자신 1 추가


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    V = E + 1  # 마지막 노드번호
    ch1 = [0] * (V + 1)  # 부모인덱스 자식1 저장
    ch2 = [0] * (V + 1)  #

    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if ch1[p] == 0:  # 자식1이 없으면
            ch1[p] = c
        else:
            ch2[p] = c
    cnt = pre_order2(N)
    print(f'#{tc} {cnt}')