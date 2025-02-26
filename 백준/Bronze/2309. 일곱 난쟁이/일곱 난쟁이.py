dwarf = [int(input()) for _ in range(9)]  # 9명의 난쟁이 키 입력

total_sum = sum(dwarf)  # 9명의 난쟁이 키 총합

# 2명의 난쟁이를 제외했을 때 합이 100이 되는 경우 찾기
for i in range(9):
    for j in range(i + 1, 9):  # i와 j가 같은 값을 가리키지 않도록 j는 i+1부터 시작
        if total_sum - dwarf[i] - dwarf[j] == 100:
            # 2명의 난쟁이를 제외한 리스트 만들기
            seven_dwarfs = [dwarf[k] for k in range(9) if k != i and k != j]
            seven_dwarfs.sort()  # 오름차순 정렬
            print("\n".join(map(str, seven_dwarfs)))  # 한 줄씩 출력
            exit()  # 정답을 찾으면 프로그램 종료
