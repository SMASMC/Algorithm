import sys

n = int(sys.stdin.readline())
temp = dict()

for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())

    # 출입
    if b == "enter":
        temp[a] = b
    # 퇴근을 했으면 삭제
    else:
        del temp[a]

temp = sorted(temp.keys(), reverse=True)

for i in temp:
    print(i)