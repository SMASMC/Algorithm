S=input()
ans=[]

for i in range(len(S)):
    ans.append(S[i:])
    
ans.sort()
print(*ans,sep='\n')