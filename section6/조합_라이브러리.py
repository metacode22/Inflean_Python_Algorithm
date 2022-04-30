import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
a = list(range(1, n + 1))
b = combinations(a, 2)
cnt = 0
for i in b:
    print(*i)
    cnt += 1
print(cnt)