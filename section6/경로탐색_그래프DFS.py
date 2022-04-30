# <나의 풀이> - 못 풀었음.
# import sys
# sys.setrecursionlimit(10**9)
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = [[0] * (n + 1) for _ in range(n + 1)]
# cnt = 0
# visited = [0] * (n + 1)
# res = [0] * 10
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
    
# def DFS(level, start):
#     global cnt, res
    
#     if start == n:      # 5번 노드에 닿았을 떄
#         cnt += 1
#         print(res)
#         return
        
#     else:
#         for k in range(1, n + 1):
#                 if graph[start][k] == 1 and visited[k] == 0:
#                     visited[k] = 1
#                     # graph[start][k] = 0
#                     # graph[k][start] = 0
#                     res[level] = k
#                     DFS(level + 1, k)
#                     visited[k] = 0
#                     # graph[start][k] = 1
#                     # graph[k][start] = 1
            
#             # if graph[] == 1:                # 이어져 있을 때
#             #     DFS(level + 1, j + 1, )
#             # else:                           # 1이 아닐 때, 즉 이어져 있지 않을 때
# visited[1] = 1
# res[0] = 1
# DFS(1, 1)
# print(cnt)



# <강의 풀이>
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
path = []
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
cnt = 0

def DFS(level):
    global cnt
    
    if level == n:
        print(*path)
        cnt += 1
        return
        
    else:
        for i in range(1, n + 1):
            if graph[level][i] == 1 and visited[i] == 0:
                visited[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                visited[i] = 0
    
visited[1] = 1      # 1번은 이미 방문했다. 1번부터 시작이니
path.append(1)      # 1번부터 시작.
DFS(1)              # 1번부터 시작.
print(cnt)


