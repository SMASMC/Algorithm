# Greedy 22:20

def solution(people, limit):
    people.sort()
    
    answer = 0
    
    left_idx = 0
    right_idx = len(people)-1
    
    while left_idx <= right_idx:
        if (people[left_idx] + people[right_idx]) <= limit:
            left_idx +=1
            right_idx -=1
            answer += 1
        else: # 그렇지 않다는것은 right_idx의 값으로만 제한 몸무게를 충족
            right_idx -= 1
            answer += 1
    return answer