import sys, heapq

input = sys.stdin.readline
n = int(input())
q = []
for i in range(n):
	num_list = list(map(int, input().split()))
	if not q: # q에 아무것도 없는 첫번째 입력 시
		for num in num_list:
			heapq.heappush(q, num) # min_heap 구조로 q 채우기
	else:
		for num in num_list:
			if q[0] < num:
				heapq.heappush(q, num)
				heapq.heappop(q)
print(q[0])