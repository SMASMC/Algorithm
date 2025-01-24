input_text=list(input())
abc='abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in input_text:
        print(input_text.index(i), end =' ')
    else:
        print(-1, end=' ')