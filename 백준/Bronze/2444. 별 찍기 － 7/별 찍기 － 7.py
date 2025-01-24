star_count=int(input())
# n => *
# n-1 => *** (1+2)
# n-2 => ***** (1+4)
for i in range(1,star_count):
    print(' '*(star_count-i)+'*'*(2*i-1))
for j in range(star_count,0,-1):
    print(' '*(star_count-j)+'*'*(2*j-1))