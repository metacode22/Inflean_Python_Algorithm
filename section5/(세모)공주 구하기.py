# deque
# append(right/left)
# pop(right/left)

from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque(range(1, n + 1))

cnt = 0
while len(queue) > 1:
    cnt += 1
    if cnt != k:
        queue.append(queue.popleft())
    elif cnt == k:
        queue.popleft()
        cnt = 0

print(queue[0])

# from collections import deque
# import sys
# # sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n, k = map(int, input().split())
# dq = list(range(1, n+1))
# dq = deque(dq)

# while dq:
#     for _ in range(k-1):
#         cur = dq.popleft()
#         dq.append(cur)
#     dq.popleft()

#     if len(dq) == 1:
#         print(dq[0])
#         dq.popleft()

