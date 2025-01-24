R= int(input())
P=''
for i in range(R):
    count, text=input().split()
    for j in text:
        P+=j*int(count)
    P+='\n'
print(P)