# 25501번 재귀의 귀재 20: 53
import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스

for tc in range(T):
    
    count = 0
    s = list(input().strip()) # 문자를 받는 리스트 변수
    def recursion(s, l, r):
        global count
        count += 1
        if (l >= r): # 조회하는 위치가 크거나 같으므로 조회 종료
            return 1
        elif (s[l] != s[r]): # 양끝이 다르므로 0을 반환
            return 0
        else:
            return recursion(s, l+1, r-1)

    def isPalindrome(s):
        return recursion(s, 0, len(s)-1) # 0부터 시작, 크기의 끝 만약 len이 5라면, s[4]까지 조회
    
    print(f'{isPalindrome(s)} {count}')
