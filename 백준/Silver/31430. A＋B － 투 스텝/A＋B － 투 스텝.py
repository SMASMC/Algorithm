t = int(input())

if t == 1:
    a, b = map(int, input().split())
    result = ''
    n = a + b
    while n > 0:
        k = n % 26
        n //= 26
        result += chr(k + ord('a'))
    result += (13 - len(result)) * 'a'
    print(result)
elif t == 2:
    s = input().strip()
    result = 0
    for i in range(len(s)):
        k = ord(s[i]) - ord('a')
        result += k * (26 ** i)
    print(result)