# 19532번 수학은 비대면 강의입니다.
# 09 : 14


# ax + by = c
# dx + ey = f
# a ,b, c, d, e, f 6개의 숫자가 공백으로 주어짐.
a, b, c, d, e, f = map(int, input().split())
# x, y는 무엇인지 맞춰야함
x, y = -999, -999
# x, y를 차례대로 증가 시켜서 c와 f를 맞추는 값을 찾으면 될 것 같다.
# 이때 x를 먼저 증가시키고, y는 놔두고, c와 f를 맞추게 된다면, 정답, c와 f보다 크게된다면,
# y를 증가시키고, x를 다시 그다음수부터 증가 2중 while이면 된다.

found = False
while x <= 999:
    y = -999
    while y <= 999 :
        if (a*x + b*y) == c and (d*x + e*y) == f:
            # 정답을 찾았으므로 답을 출력하고, 중지한다.
            print(x, y)
            found = True
            break
        y += 1
    if found:
        break
    x += 1