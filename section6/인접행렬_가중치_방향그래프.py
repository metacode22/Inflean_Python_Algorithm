# <나의 풀이> - 무방향 그래프
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n, m = map(int, input().split())
# mat = [[0] * n for _ in range(n)]
# a = list()

# for _ in range(m):
#     a.append(list(map(int, input().split())))
    
# for i in range(m):
#     x = a[i][0] - 1
#     y = a[i][1] - 1
    
#     mat[x][y] = 1
#     mat[y][x] = 1
    
# for x in mat:
#     print(x)
    
# <나의 풀이> - 방향 그래프
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n, m = map(int, input().split())
# a = list()
# for _ in range(m):
#     a.append(list(map(int, input().split())))

# mat = [[0] * (n + 1) for _ in range(n + 1)]

# for i in range(m):
#     x = a[i][0]
#     y = a[i][1]
#     mat[x][y] = a[i][2]
    
# for j in range(1, n + 1):
#     for k in range(1, n + 1):
#         print(mat[j][k], end = ' ')
#     print()



# <강의 풀이> - 무방향 그래프
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = [[0] * (n + 1) for _ in range(n + 1)]

# for i in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1
    
# for j in range(1, n + 1):
#     for k in range(1, n + 1):
#         print(graph[j][k], end = ' ')
#     print()

# <강의 풀이> - 방향 그래프
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = [[0] * (n + 1) for _ in range(n + 1)]

# for i in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
    
# for j in range(1, n + 1):
#     for k in range(1, n + 1):
#         print(graph[j][k], end = ' ')
#     print()
    




