# 3052번: 나머지

# count가 있으면 +1 없으면 다음으로 넘어가면 됨.
count=0
remainder=[]
for _ in range(10):
    number=int(input())
    remainder.append(number%42)
    if remainder.count(number%42)==1:
        count+=1
print(count)