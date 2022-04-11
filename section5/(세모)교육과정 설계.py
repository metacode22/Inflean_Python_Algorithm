# import sys
# from collections import deque
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# check = deque(list(map(str, input().rstrip())))
# n = int(input())

# for j in range(n):
#     need = check.copy()
#     sub = list(map(str, input().rstrip()))

#     for i in sub:
#         if need:
#             if i == need[0]:
#                 need.popleft()
#             elif i != need[0] and i in need:
#                 break

#     if not need:
#         print(f'#{j + 1} YES')
#     else:
#         print(f'#{j + 1} NO')

import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline

need = input().rstrip()
n = int(input())

for i in range(n):
    plan = input().rstrip()
    dq = deque(need)

    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print(f'#{i + 1} NO')
                break
    else:
        if len(dq) == 0:
            print(f'#{i + 1} YES')