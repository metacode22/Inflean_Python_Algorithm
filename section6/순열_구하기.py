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
            if visited[i] == 0:     # 1일 경우, 앞에서 사용했다는 의미이므로 다음 재귀를 들어가지 못하게 한다.
                visited[i] = 1      # 따라서 n이 3일 때 9번 찍혀야 될 것이 6번 찍히게 된다.
                res[level] = i      # 그냥 들어가면 중복 순열처럼 1 1도 찍히게 된다.
                DFS(level + 1)
                visited[i] = 0

DFS(0)
print(cnt)