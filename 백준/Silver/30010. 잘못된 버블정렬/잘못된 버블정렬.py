N = int(input())

# 반례가 되는 수열 생성
result = [N] + list(range(1, N))

# 패킹으로 묶어서 출력
print(*result)