import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
def topology_sort():
    result = list()
    q = deque()
    for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)
    while q:
        
        now = q.popleft()
        result.append(now)
                
        for j in graph[now]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)
                
    for l in result:
        print(l , end = ' ')
        
topology_sort()
        