import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def DFS(level):
    if level == m:
        return
    
    else:
        for i in range(1, n + 1):
            res[level] = i
            DFS(level + 1)

n, m = map(int, input().split())
res = [0] * m
cnt = 0
DFS(0)
print(cnt)