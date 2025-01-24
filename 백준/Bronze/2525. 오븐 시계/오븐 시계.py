hour, minute = map(int,input().split())

plus_minute=int(input())

hour +=(plus_minute+minute)//60
minute += plus_minute % 60

if minute >=60:
    minute-=60
if hour >=24:
    hour%=24

print(hour, minute)