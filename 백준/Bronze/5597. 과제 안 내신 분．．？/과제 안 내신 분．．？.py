# 5597번: 과제 안 내신 분..?

studentNumber=[]
notStudentNumber=[]
for _ in range(28):
    # studentNumber.append(map(int,input()))
    # s=
    studentNumber.append(int(input()))
for _ in range(1,31):
    
    if _ not in studentNumber:
        notStudentNumber.append(_)

print(min(notStudentNumber))
print(max(notStudentNumber))