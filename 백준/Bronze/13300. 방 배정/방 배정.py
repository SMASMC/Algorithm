# 09 : 50
N, K = map(int,input().split()) # N 학생수, K 최대 인원 수

student = list([0,0] for _ in range(6))
room_cnt =0

for n in range(N):
    S, grade = map(int, input().split()) # S 성별 female 0, male 1, grade 등급
    student[grade-1][S] +=1
    if student[grade-1][S] == 1:
        room_cnt +=1
    if student[grade-1][S] == K: # 최대 인원수를 채웠으므로, count할 수 있도록 0으로 초기화
        student[grade-1][S] = 0
print(room_cnt)