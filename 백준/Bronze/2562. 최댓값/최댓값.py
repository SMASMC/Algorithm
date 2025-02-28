# 2562번: 최댓값

numbers=[]
for i in range(9):
    numbers.append(int(input()))

maximum=max(numbers)
print(maximum)
print(numbers.index(maximum)+1)