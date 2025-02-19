# 2292번 벌집
# 13 :58 시작

# 벌집은 n * 6 만큼 증가한다.
N = int(input()) # 벌집의 위치
bee_n = 1
n = 1
while bee_n < N:
    bee_n += 6*n
    n += 1

print(n)