A, B, V = map(int, input().split()) # A : 올라가기, B : 내려가기, V : 꼭대기
day = 0
if (V - B) % (A - B) ==0:
    day = (V - B) // (A - B)
else:
    day = (V - B) // (A - B) + 1

print(day)