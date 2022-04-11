import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

k, n = map(int, input().split())
line = []
largest = 0
for _ in range(k):
    tmp = int(input())
    line.append(tmp)
    if tmp > largest:
        largest = tmp

def count(len):
    cnt = 0
    for i in line:
        cnt += i // len

    return cnt

lt = 1
rt = largest
res = 0
while lt <= rt:
    mid = (lt + rt) // 2

    if count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)