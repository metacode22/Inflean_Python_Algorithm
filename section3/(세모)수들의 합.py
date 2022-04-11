import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:                         # tot이 m도 아닌데, m 가까이 못갔는데,
        if rt < n:
            tot += a[rt]
            rt += 1
        else:                           # rt가 n을 넘어도(lt로부터 끝까지 더했어도) m이 되는 숫자를 못찼았다면
            break                       # 가망이 없다는 것이니 탐색을 끝낸다.

    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1

    else:
        tot -= a[lt]
        lt += 1

print(cnt)