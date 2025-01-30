# 크로아티아 알파벳 포함 알파벳의 숫자를 셈하는 알고리즘

# 크로아티아 알파벳 c=, c-,dz=,d-,lj,nj,s=,z=
# 값을 입력받고, split(크로아티아 알파벳[0]) 이런식으로 끊어내고,
# 나머지 알파벳을 묶어서 숫자로 셈하면 될 것 같음.
croatia_alphabet_list=["c=", "c-","dz=","d-","lj","nj","s=","z="]
alphabet=input() # ljes=njak

for ca in croatia_alphabet_list:
    # croatia_alphabet=alphabet.split(ca)
        alphabet=alphabet.replace(ca,'*') # input 변수와 동일한 이름의 변수를 *로 변경


print(len(alphabet))