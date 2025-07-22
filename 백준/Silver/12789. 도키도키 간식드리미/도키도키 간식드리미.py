N = int(input()) # 학생들의 수

student_number_arr = list(map(int,input().split()))

# 승환이가 무사히 간식을 받는다면 Nice, 아니라면 Sad


# stack을 이용해서 왼쪽으로 순차적으로 보낼 수 있다면 Nice, 아니라면 Sad
# 1부터 순차적으로 작은 수들을 찾기 위해서 오른쪽(현재 줄 서는 곳)으로 보내고,
# 1부터 순차적으로 작은 수들을 찾으면 왼쪽(간식 받는 곳)으로 보낸다.
# 보낸 뒤, 다시 한 명씩만 설 수 있는 공간으로 보낸다.

middle_line = [] # 이 라인에는 순차적으로 쌓아야한다. 만약 줄어드는 값으로 쌓이지 않으면 False

pass_number=1 # 왼쪽으로 통과되는 숫자

for student in student_number_arr:
    if student == pass_number:
        pass_number +=1
    else:
        middle_line.append(student)
    
    # middle_line이 있고, top이 pass_number와 같다면,
    while middle_line and middle_line[-1] == pass_number:
        middle_line.pop() # top에서 제거
        pass_number +=1
                
if pass_number == N + 1: # 참이면 Nice, 거짓이면 Sad
    print("Nice")
else:
    print("Sad")