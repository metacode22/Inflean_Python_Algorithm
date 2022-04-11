import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0

while True:
    cur = Q.popleft()

    if any(cur[1] < x[1] for x in Q):           # any, 1개라도 참이면
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break

# import sys
# from collections import deque
# # sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n, m = map(int, input().split())
# a = [(idx, val) for idx, val in enumerate(list(map(int, input().split())))]
# queue = deque(a)
# cnt = 0

# while True:
#     max = queue[0][1]

#     for i in range(1, len(queue)):
#         if max < queue[i][1]:
#             max = queue[i][1]

#     if max == queue[0][1] and queue[0][0] == m:
#         cnt += 1
#         print(cnt)
#         queue.popleft()
#         break

#     elif max == queue[0][1]:
#         cnt += 1
#         queue.popleft()

#     else:
#         queue.append(queue.popleft())