import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')
        return
        
DFS(n)