test_case_count=int(input())
text_str=''

for i in range(0,test_case_count):
    text=input()
    text_str+=(text[0]+text[-1]+'\n')

print(text_str)