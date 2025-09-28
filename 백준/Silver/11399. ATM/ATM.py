N = int(input())
peoples = list(map(int, input().split()))  # 기다리는 사람들 입력 받음
peoples.sort()  # 작은 순서대로 정렬
answer = 0

for x in range(1, N+1):
    answer += sum(peoples[0:x])
print(answer)  # 정답 제출