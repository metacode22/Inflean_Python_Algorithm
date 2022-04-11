import sys

n, m = map(int, sys.stdin.readline().split())
arr = [0 for _ in range(n + m + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        arr[i + j] += 1

max = 0
for k in range(2, len(arr)):
    if arr[k] > max:
        max = arr[k]

for l in range(2, len(arr)):
    if arr[l] == max:
        print(l, end=' ')