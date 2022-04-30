import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
bricks = list()
for _ in range(n):
    width, height, mass = map(int, input().split())
    bricks.append((width, height, mass))
bricks.sort(reverse=True)
dy = [0] * n
dy[0] = bricks[0][1]
res = 0

for i in range(1, n):
    max_h = 0
    
    for j in range(i - 1, -1, -1):
        if bricks[i][2] < bricks[j][2] and dy[j] > max_h:
            max_h = dy[j]
            
    dy[i] = max_h + bricks[i][1]
    if dy[i] > res:
        res = dy[i]
        
print(res)

    
