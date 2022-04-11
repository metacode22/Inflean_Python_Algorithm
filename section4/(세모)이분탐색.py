import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

lt = 0
rt = n - 1
mid = (lt + rt)//2

while True:
    if a[mid] == m:
        print(mid + 1)
        break

    elif a[mid] > m:
        rt = mid - 1
        mid = (lt + rt)//2

    else:
        lt = mid + 1
        mid = (lt + rt)//2