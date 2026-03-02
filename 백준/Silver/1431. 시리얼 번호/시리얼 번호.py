import sys

def sum_num(num):
    res = 0
    for word in num:
        if word.isdigit():
            res += int(word)
    return res

n = int(sys.stdin.readline())
m = [list(sys.stdin.readline().strip()) for _ in range(n)]
m.sort(key=lambda x: (len(x), sum_num(x), x))
for i in m:
    print("".join(i))