import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [0] * (n + 1)
res = [0] * m
cnt = 0

def DFS(level):
    global cnt
    
    if level == m:
        for j in range(m):
            print(res[j], end = ' ')
        print()
        cnt += 1
        return
        
    else:
        for i in range(1, n + 1):
            if visited[i] == 0:
                visited[i] = 1
                res[level] = i
                DFS(level + 1)
                visited[i] = 0
            
DFS(0)
print(cnt)
