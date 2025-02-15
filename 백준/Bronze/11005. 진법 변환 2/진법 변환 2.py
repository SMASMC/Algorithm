# 11005 진법 변환 2

N, B = map(int,input().split())

# N에 들어온 값을 B진법 (A~Z)으로 변경하는 프로그램이다.

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''
# 여기서 B를 이용하여 무엇을 나누거나, 곱해서 N을 출력할 수 있을지 고민해보자

while N:
    result += str(alphabet[N%B])
    N //= B

print(result[::-1])