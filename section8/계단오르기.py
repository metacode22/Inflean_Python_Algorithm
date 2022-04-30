import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
d = [0] * (n + 1)

def DFS(x):
    if d[x] != 0:
        return d[x]
    
    if x == 1 or x == 2:
        return x
        
    else:
        d[x] = DFS(x - 1) + DFS(x - 2)
        return d[x]
        
print(DFS(n))