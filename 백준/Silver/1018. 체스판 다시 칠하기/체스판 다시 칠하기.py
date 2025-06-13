n,m=map(int,input().split())

mtr=[]
cnt=[]
for i in range(n):
    mtr.append(input())
    
for i in range(n-7):
    for j in range(m-7):
        w=0 #흰색
        b=0 #검은색
        for ai in range(i,i+8):
            for aj in range(j,j+8):
                if (ai+aj)%2==0:
                    if mtr[ai][aj]!='W':# W가 아니면, 즉 B이면
                        w+=1# W로 칠하는 갯수
                    else:
                        b+=1
                else:#홀수인 경우
                    if mtr[ai][aj]!='W':# W가 아니면, 즉 B이면
                        b+=1# B로 칠하는 갯수
                    else:
                        w+=1# W로 칠하는 갯수
                        
        cnt.append(w) #W로 시작할 때 경우의 수
        cnt.append(b) #B로 시작할 때 경우의 수
print(min(cnt))