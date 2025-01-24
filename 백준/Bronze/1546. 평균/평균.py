# 1546번: 평균

n=int(input()) # 과목의 개수

score = list(map(int,input().split()))
m=max(score)
for i in range(len(score)):
    score[i]=score[i]/m*100

print(sum(score)/len(score))