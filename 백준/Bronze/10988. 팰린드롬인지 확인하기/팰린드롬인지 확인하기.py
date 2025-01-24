# 팰린드롬 : 순서를 거꾸로 읽었을 때도 원래의 문자열이나 수열과 동일한 경우를 의미함.
# 토마토, eye, kayak 등


word_palindrome = input()

if word_palindrome[::-1] == word_palindrome:
    print(1)
else:
    print(0)