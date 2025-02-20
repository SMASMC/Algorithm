num1 = int(input())
num2 = input()
num2_arr = list(map(int, num2))

for i in range(len(num2_arr)-1,-1,-1):
    print(num1 * num2_arr[i])

print(num1* int(num2))