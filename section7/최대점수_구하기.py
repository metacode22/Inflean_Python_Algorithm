import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
score_inp = list()
time_inp = list()
for _ in range(n):
    a, b = map(int, input().split())
    score_inp.append(a)
    time_inp.append(b)
res = -2147000000
    
def DFS(level, score, time):
    global res
    
    if time > m:
        return
    
    if level == n:
        if score > res:
            res = score
        return
        
    else:
        DFS(level + 1, score + score_inp[level], time + time_inp[level])
        DFS(level + 1, score, time)
        
DFS(0, 0, 0)
print(res)