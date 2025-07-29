def solution(progresses, speeds):
    # speeds가 주어지면, 각 배포마다 몇 개의 기능이 배포되는지 return
    # progresses와 speeds를 이용해서 각 speeds가 progresses를 언제 끝낼 수 있는지를
    # return에 담고 반환하는 프로그램.
    # 앞에 있는 기능이 먼저 배포되어야 배포를 할 수 있음
    answer = []
    hundred_res = [] # 100을 넘긴 count 횟수를 배열로 저장
    for i in range(len(progresses)):
        speed_count = 0 # 몇번 speeds를 반복했는지 확인
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            speed_count +=1
        # speed_count가 이전보다 작으면 이전 크기를 저장시킨다.
        if hundred_res and hundred_res[-1] >= speed_count:
            hundred_res.append(hundred_res[-1])
            answer[-1]+=1
        else:
            hundred_res.append(speed_count)
            answer.append(1)
    return answer