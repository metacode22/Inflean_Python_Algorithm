# <나의 풀이>
import sys
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0

c = combinations(a, k)
for i in c:
    if sum(i) % m == 0:
        cnt += 1

print(cnt)



# <강의 풀이>
import sys
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0

for x in combinations(a, k):
    if sum(x) % m == 0:
        cnt += 1
print(cnt)
