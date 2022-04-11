import sys

t = int(sys.stdin.readline())

for i in range(t):
    n, s, e, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    tmp = arr[s - 1 : e]
    tmp.sort()

    print(f'#{i+1}', tmp[k - 1])