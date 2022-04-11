import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

def count(len):
    cnt = 1
    tot = 0

    for x in a:
        if tot + x > len:
            cnt += 1
            tot = x
        else:
            tot += x

    return cnt

lt = 1
rt = sum(a)
res = 0
while lt <= rt:
    mid = (lt+rt) // 2
    if mid >= max(a) and count(mid) <= m:
        rt = mid - 1
        res = mid
    else:
        # count(mid) > m
        lt = mid + 1

print(res)