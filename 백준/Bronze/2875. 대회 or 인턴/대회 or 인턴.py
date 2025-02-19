# 2875번 대회 or 인턴
# 여2, 남1 으로 구성된 팀 1
N, M, K = map(int, input().split()) # N 여, M 남, K 참여해야하는 학생 수
team_count = 0
woman = N
man = M
while (woman + man - K >= 3) and (woman >=2 and man >=1): # 팀으로된 인원수가 인턴으로 빠진 인원보다 작을 경우와 여,남이 다 있을 경우까지
    woman -=2
    man -=1
    if woman >= 0 and man >= 0: # 마지막 인원까지 team으로 count한다.
        team_count+=1

print(team_count)