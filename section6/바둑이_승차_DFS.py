# <나의 풀이>
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# c, n = map(int, input().split())
# w = list()
# for _ in range(n):
#     w.append(int(input()))
# check_list = [0] * n
# res = []

# def DFS(level):
#     if level == n:
#         tmp = 0
#         for i in range(0, len(w)):
#             if check_list[i] == 1:
#                tmp += w[i]  
               
#         if tmp < c:
#             res.append(tmp)
#         return
    
#     else:
#         check_list[level] = 1
#         DFS(level + 1)
#         check_list[level] = 0
#         DFS(level + 1)

# DFS(0)
# print(max(res))

# <강의 풀이>
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

c, n = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
res = -2147000000
total = sum(a)

# tsum은 부분집합에 넣든 안넣든 판단했던 것들을 모두 더한 것.
# sum은 실제로 더한 것.
# total - tsum은 판단한 것들을 제외하고 남은 것들
# 판단해서 실제로 더한 것과, 아직 남은 것들을 !미리! 더해보고 기존에 구한 res보다 작으면 바로 종료.
# 밑으로 내려갈 필요가 없다고 판단. 
def DFS(level, sum, tsum):
    global res
    if total - tsum + sum < res:
        return
    
    if sum > c:
        return
    
    if level == n:
        if res < sum < c:
            res = sum
    
    else:
        DFS(level + 1, sum + a[level], tsum + a[level])
        DFS(level + 1, sum, tsum + a[level])
        
DFS(0, 0, 0)
print(res)
