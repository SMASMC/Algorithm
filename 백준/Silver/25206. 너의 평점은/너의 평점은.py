grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0','D+','D0','F']
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

total = 0
result_avg=0

for i in range(20):
    sub, sco, gra=input().split()
    if gra in grade:
        if gra == 'P':
            continue
        total+=float(sco)
        result_avg+=float(sco)*score[grade.index(gra)]
        
map_score_grade=(result_avg/total)

print(round(map_score_grade,6))