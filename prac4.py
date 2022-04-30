import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
coin = list(map(int, input().split()))
cost = int(input())
coin.sort(reverse = True)
res = float('inf')

def DFS(level, sum):
    global res
    if level > res:
        return
    
    if sum > cost:
        return
        
    if sum == cost:
        if level < res:
            res = level
        return
    
    else:
        for i in range(n):
            DFS(level + 1, sum + coin[i])
    
DFS(0, 0)
print(res)