import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = 0
sum = 0

for i in arr:
    if i == 1:
        sum += 1
        res += sum
    if i == 0:
        sum = 0

print(res)
