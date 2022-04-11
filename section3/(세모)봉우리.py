import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1 , 0, 1, 0]
dy = [0, 1, 0 , -1]

a.insert(0, [0] * n)
a.append([0] * n)

for i in a:
    i.insert(0, 0)
    i.append(0)

cnt = 0
for j in range(1, n + 1):
    for k in range(1, n + 1):
        # if a[j][k] > a[j][k - 1] and a[j][k] > a[j][k + 1] and a[j][k] > a[j - 1][k] and a[j][k] > a[j + 1][k]:
        #     cnt += 1

        if all(a[j][k] > a[j + dx[l]][k + dy[l]] for l in range(4)):
            cnt += 1

print(cnt)