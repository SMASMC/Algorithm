import sys
m,n=map(int,sys.stdin.readline().split())
snack=list(map(int,sys.stdin.readline().split()))

start=1
end=max(snack)

answer=0
while start<=end:
    mid=(start+end)//2 

    cnt=0
    for x in snack:
        if x<mid:
            continue
        else:
            cnt+=x//mid

    if cnt>=m:
        start=mid+1
        answer=mid
    else:
        end=mid-1

print(answer)