n = int(input())
cnt = 0
# 1666, 2666, 3666 등으로 정의
# 1 = 666, 2 = 1666, 3 = 2666 ...
result = 666
i = 0
while True : # 666을 포함하는 수를 찾아서 count 하면 됨
    i += 1
    if '666' in str(i):
        cnt +=1
        if cnt == n:
            result = i
            break

print(result)