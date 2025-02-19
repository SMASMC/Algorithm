# 2875 번 대회 or 인턴

N, M, K = map(int,input().split()) # N 여학생, M 남학생, K 인턴쉽

team_count = 0
while (N + M - K >= 3) and (N>=2 and M>=1):
    N-=2
    M-=1
    team_count+=1
    
print(team_count)