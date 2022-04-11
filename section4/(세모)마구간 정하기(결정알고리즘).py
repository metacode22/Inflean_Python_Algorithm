import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n, c = map(int, input().split())
line = []
for _ in range(n):
    line.append(int(input()))
line.sort()

# line = [1 ,2 , 4, 8, 9]
def count(len):
    ep = line[0]
    cnt = 1

    for i in range(1, n):
        if line[i] - ep >= len:
            cnt += 1
            ep = line[i]

    return cnt

lt = 1
rt = line[n - 1] - line[0]
res = 0
while lt <= rt:
    mid = (lt+rt) // 2
    if count(mid) >= c:
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1

print(res)