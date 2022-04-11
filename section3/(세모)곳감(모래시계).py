import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for _ in range(m):
    r, t, k = map(int, input().split())

    if t == 0:
        for _ in range(k):
            a[r - 1].append(a[r - 1].pop(0))
    else:
        for _ in range(k):
            a[r - 1].insert(0, a[r - 1].pop())

s = 0
e = n - 1
res = 0

for i in range(n):
    for j in range(s, e + 1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1