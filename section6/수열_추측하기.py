# <나의 풀이>
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, f = map(int, input().split())
a = list(range(1, n + 1))
sub = [1] * n
for i in range(1, n - 1):
    sub[i] = sub[i - 1] * (n - i)//i
visited = [0] * (n + 1)
res = [0] * (n)
sum = 0

def DFS(level):
    global sum
    
    if level == n:
        for k in range(n):
            sum += res[k] * sub[k]
        
        if sum == f:
            print(*res)
            sys.exit(0)
        else:
            sum = 0
            
        return
    else:
        for j in range(1, n + 1):
            if visited[j] == 0:
                visited[j] = 1
                res[level] = j
                DFS(level + 1)
                visited[j] = 0

DFS(0)



# <강의 풀이>
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, f = map(int, input().split())
visited = [0] * (n + 1)       # 중복을 방지하기 위한 체크리스트
p = [0] * n                   # permutation, 순열
b = [1] * n                   # 이항 계수가 될 배열로, 1로 초기화 해둠.
for i in range(1, n):         # 이항계수화
    b[i] = b[i - 1]*(n - i)//i

def DFS(level, sum):
    if level == n and sum == f:
        for x in p:
            print(x, end = ' ')
        sys.exit(0)
        return
    
    else:
        for i in range(1, n + 1):
            if visited[i] == 0:
                visited[i] = 1
                p[level] = i
                DFS(level + 1, sum + p[level] * b[level])       # 더하는 과정 필요없이 한 번에 구할 수 있음
                visited[i] = 0
                
DFS(0, 0)