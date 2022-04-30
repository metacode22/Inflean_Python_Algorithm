# <나의 풀이>
# import sys
# from itertools import permutations
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n, f = map(int, input().split())
# a = list(range(1, n + 1))
# p = permutations(a, n)
# sub = [1] * n
# for i in range(1, n - 1):
#     sub[i] = sub[i - 1]*(n - i)//i
    
# for j in p:
#     sum = 0
#     for k in range(n):
#         sum += j[k] * sub[k]
#     if sum == f:
#         print(*j)
#         break



# <강의 풀이>
import sys
from itertools import permutations
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, f = map(int, input().split())
a = list(range(1, n + 1))
sub = [1] * n
for i in range(1, n - 1):
    sub[i] = sub[i - 1]*(n - i)//i
    
for tmp in permutations(a):
    sum = 0
    # print(tmp)
    for L, x in enumerate(tmp):
        sum += x*sub[L]
    
    if sum == f:
        for j in range(n):
            print(tmp[j], end = ' ')
        break                           # 36행의 for문을 중지시킨다.