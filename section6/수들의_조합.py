# <나의 풀이>
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# a.insert(0, 0)
# m = int(input())
# cnt = 0
# res = [0] * n
            
# def DFS(level, start, sum):
#     global cnt
    
#     if level == k:
#         for j in range(k):
#             print(res[j], end = ' ')
#         print()
        
#         if sum % m == 0:
#             cnt += 1
#         return
        
#     else:
#         for i in range(start, n + 1):
#             res[level] = a[i]
#             DFS(level + 1, i + 1, sum + a[i])
            
# DFS(0, 1, 0)
# print(cnt)



# 강의 풀이
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0
res = [0] * k
def DFS(level, start, sum):
    global cnt
    
    if level == k:
        # print(res)
        if sum % m == 0:
            cnt += 1
        return
        
    else:
        for i in range(start, n):               # a라는 배열에서 값을 가져오므로 0부터 n - 1 까지 돌아야 한다.
            # res[level] = a[i]
            DFS(level + 1, i + 1, sum + a[i])   # start라는 인수를 따로 준다.
                                                # 겹치지 않도록 start를 뒤로 한 칸씩 미룬다. 
DFS(0, 0, 0)                                    # 그냥 i를 넘겨주면 2 2와 같이 중복된 수열이 나오게 된다.
print(cnt)