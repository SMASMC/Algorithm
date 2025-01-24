# 같은 눈 3개 10,000 => (같은 눈) x 1,000
# 같은 눈이 2개만 나오는 경우에는 1,000원 + (같은 눈) x 100
# 모두 다른 눈만 나오는 경우 (그 중 가장 큰 눈)x 100

dice = list(map(int,input().split()))
prizes=0

if dice[0] == dice[1] == dice[2]:
    prizes=10000+(dice[0]*1000)
elif dice[0] ==dice[1]:
    prizes=1000+(dice[0]*100)
elif dice[0] == dice[2]:
    prizes=1000+(dice[0]*100)
elif dice[1] == dice[2]:
    prizes=1000+(dice[1]*100)
else:
    prizes=(max(dice)*100)
print(prizes)