# 백준 스위치 켜고 끄기
N = int(input())  # 스위치 개수
switch_arr = list(map(int, input().split()))  # 스위치 초기 상태
student_count = int(input())  # 학생 수

for _ in range(student_count):
    gender, switch_num = map(int, input().split())  # 성별(1: 남, 2: 여), 스위치 번호

    if gender == 1:  # 남학생: 입력받은 수의 배수를 반전
        for i in range(switch_num, N+1, switch_num):  
            switch_arr[i-1] = 1 - switch_arr[i-1]  # 0 <-> 1 토글

    elif gender == 2:  # 여학생: 좌우 대칭 반전
        switch_arr[switch_num - 1] = 1 - switch_arr[switch_num - 1]  # 중앙 반전
        
        lr_count = 1
        while (switch_num - 1 - lr_count >= 0) and (switch_num - 1 + lr_count < N) and \
              (switch_arr[switch_num - 1 - lr_count] == switch_arr[switch_num - 1 + lr_count]):
            switch_arr[switch_num - 1 - lr_count] = 1 - switch_arr[switch_num - 1 - lr_count]
            switch_arr[switch_num - 1 + lr_count] = 1 - switch_arr[switch_num - 1 + lr_count]
            lr_count += 1  # 좌우 확장

# 한 줄에 20개씩 출력 (문제 요구 사항)
for i in range(0, N, 20):
    print(*switch_arr[i:i+20])
