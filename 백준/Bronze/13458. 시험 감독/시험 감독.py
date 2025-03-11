# 13458 시험 감독 15 : 57

N = int(input()) # 총 N개의 시험장 수


Ai = list(map(int, input().split()))# 각 반에 있는 응시자 수
B, C = map(int, input().split())
student_cnt = 0
for n in range(N):
    num = Ai[n] # Ai에 n번째에 있는 값을 부여
    num -= B
    student_cnt += 1
    if num > 0:
        if num % C == 0:
            student_cnt += (num // C)
        else:
            student_cnt += (num // C + 1)
print(student_cnt)