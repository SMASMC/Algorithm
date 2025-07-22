def solution(arr): # arr에서 연속적으로 나타나는 숫자를 제거하고, 남은 수들을 return 하는 함수
    answer = [arr[0]]
    
    stack_arr = []
    
    for a in arr:
        if stack_arr and stack_arr[-1] != a : # stack_arr이 있고, 마지막 값이 a와 다르면 쌓겠다.
            answer.append(a)
        stack_arr.append(a)
    # print(answer)
    return answer
# def solution(arr):
#     ans = [arr[0]]
#     for i in range(1, len(arr)):
#         if arr[i] != arr[i-1]:
#             ans.append(arr[i])
#     return ans