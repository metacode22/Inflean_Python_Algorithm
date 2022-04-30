# # <나의 풀이>
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n = int(input())
# meeting = list()
# for _ in range(n):
#     start, end = map(int, input().split())
#     meeting.append([start, end])
# meeting.sort(key = lambda x:x[1])
# res = list()
# res.append(meeting[0])

# for i in range(1, n):
#     if meeting[i][0] >= res[-1][1]:
#         res.append(meeting[i])

# print(len(res))



# <강의 풀이>
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
meeting = list()
for _ in range(n):
    start, end = map(int, input().split())
    meeting.append([start, end])
meeting.sort(key = lambda x:[x[1], x[0]])
cnt = 0
end = 0

for s, e in meeting:
    if s >= end:
        end = e
        cnt += 1
        
print(cnt)
