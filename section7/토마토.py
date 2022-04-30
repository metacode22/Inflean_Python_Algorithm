import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

m, n = map(int, input().split())
tomato = list()
for _ in range(n):
    tomato.append(list(map(int, input().split())))
dis = [[-1] * m for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j))
            dis[i][j] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and dis[nx][ny] == -1 and tomato[nx][ny] == 0:
            tomato[nx][ny] = 1
            dis[nx][ny] = dis[x][y] + 1
            q.append((nx, ny))
           
res = -2147000000
for i in range(n):
    for j in range(m):
        if dis[i][j] > res:
            res = dis[i][j]
        if tomato[i][j] == 0:
            print(-1)
            sys.exit(0)
            
print(res - 1)

