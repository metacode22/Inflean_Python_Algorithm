# # Bottom-Up
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]
# dy = [[0] * n for _ in range(n)]
# dy[0][0] = board[0][0]

# for i in range(1, n):
#     dy[i][0] = dy[i - 1][0] + board[i][0]
#     dy[0][i] = dy[0][i - 1] + board[0][i]
    
# for i in range(1, n):
#     for j in range(1, n):
#         dy[i][j] = min(dy[i - 1][j], dy[i][j - 1]) + board[i][j]
        
# print(dy[n - 1][n - 1])

# Top-Down
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def DFS(x, y):
    if dp[x][y] > 0:
        return dp[x][y]
    
    if x == 0 and y == 0:
        return board[x][y]
        
    elif x == 0:
        return DFS(x, y - 1) + board[x][y]
    
    elif y == 0:
        return DFS(x - 1, y) + board[x][y]
        
    else:
        dp[x][y] = min(DFS(x, y - 1), DFS(x - 1, y)) + board[x][y]
        return dp[x][y]
        
print(DFS(n - 1, n - 1))