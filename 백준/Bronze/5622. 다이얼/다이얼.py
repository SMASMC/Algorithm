dial_number=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']


input_number=input() # AD


index_number=0
for i in range(len(input_number)): # 0
    for j in dial_number: # ABC
        if input_number[i] in j: # A가 ABC에 있다.
            index_number+=dial_number.index(j) + 3
print(index_number)