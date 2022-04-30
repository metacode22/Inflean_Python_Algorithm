import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(reverse=True)
max_weight = -sys.maxsize
cnt = 0

for height, weight in data:
    if weight > max_weight:
        max_weight = weight
        
    if weight < max_weight:
        cnt += 1
    
print(n - cnt)