yut_nori = [list(map(int,input().split())) for _ in range(3)]

result = []
for i in range(3):
    yut_count = 0
    for j in range(4):
        if yut_nori[i][j] == 1:
            yut_count+=1
    if yut_count == 1:
        result.append('C')
    elif yut_count == 2:
        result.append('B')
    elif yut_count == 3:
        result.append('A')
    elif yut_count == 4:
        result.append('E')
    else:
        result.append('D')

for re in result:
    print(re)