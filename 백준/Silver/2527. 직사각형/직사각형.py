# 직사각형
# 왼쪽 아래 꼭짓점 좌표 (x, y)
# 오른쪽 위 꼭짓점 좌표 (p, q)
# x < p, y< q이다
# (3,2) (9,8)
# ex) 3 2 9 8
# 두 직사각형의 겹치거나 겹치지 않는지 확인하여 코드 문자로 출력하는 프로그램을 구현하라

for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())

    # 공통된 부분이 없음
    if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
        print('d')
        continue

    elif x1==p2 or x2==p1:
        # 점으로 연결
        if q1==y2 or q2==y1:
            print('c')
            continue
        # 선으로 연결
        else:
            print('b')
            continue
    elif q1==y2 or q2==y1:
        # 선으로 연결
        print('b')
        continue

    # 직사각형으로 연결
    else:
        print('a')
        continue
