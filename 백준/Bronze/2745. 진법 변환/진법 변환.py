# 2745번 진법 변환
# B 진법 수 N이 주어짐 이 수를 10진법으로 바꿔 출력하는 프로그램

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 2<= B <= 36 

N, B = input().split() # ZZZZZ 36
B = int(B)
sum_num = 0
for i in range(len(N)-1, -1, -1):
    find_idx = alphabet.index(N[i]) # Z는 어디에 있는지 확인 => 26으로 나올 것을 예상

    sum_num +=(B**(len(N)-1 -i))*find_idx
print(sum_num)