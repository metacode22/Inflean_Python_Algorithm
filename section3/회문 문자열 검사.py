# 거꾸로 읽어도 똑같으면 회문 문자열.
# s가 'level'이라고 쳤을 때, le를 넘어 굳이 v, e, l까지 가지 않아도 된다.

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    s = input().rstrip().upper()
    size = len(s)

    for j in range(size//2):
        if s[j] != s[-j - 1]:
            print(f'#{i + 1} NO')
            break
    else:
        print(f'#{i + 1} YES')