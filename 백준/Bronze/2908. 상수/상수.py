text_numbers=list(input().split())

numbers=[]
for big_number in text_numbers:
    
    numbers.append(int(big_number[::-1]))
if numbers[0] <numbers[1]:
    print(numbers[1])
elif numbers[0] > numbers[1]:
    print(numbers[0])