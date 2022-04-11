import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
res = set()

for i in range(n):
    for j in range(i + 1, n):
        for l in range(j + 1, n):
            res.add(arr[i] + arr[j] + arr[l])

res = list(res)
res.sort(reverse=True)
print(res[k - 1])
