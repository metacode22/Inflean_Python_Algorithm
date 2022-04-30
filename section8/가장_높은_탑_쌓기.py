# 밑면이 넓은 벽돌을 아래에서부터
# 무게가 무거운 것을 아래에서부터

# <나의 풀이, 정답 X>
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n = int(input())
# bricks = list()
# for _ in range(n):
#     width, height, mass = map(int, input().split())
#     bricks.append([width, height, mass])
# bricks.insert(0, [0, 0, 0])
# dy = [0] * (n + 1)
# dy[1] = 1
# res = bricks[1][1]

# for i in range(2, n + 1):
#     max = 0
    
#     for j in range(i - 1, 0, -1):
#         if bricks[i][0] < bricks[j][0] and bricks[i][2] < bricks[j][2] and dy[j] > max:
#             max = dy[j]
#             dy[i] = max + 1
#             res += bricks[i][1]
#             break
#     else:
#         dy[i] = dy[i - 1]
    
# print(dy)
# print(res)



# <강의 풀이>
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
bricks = list()
for i in range(n):
    a, b, c = map(int, input().split())
    bricks.append((a, b, c, i))
bricks.sort(reverse=True)
dy = [0] * n
dy[0] = bricks[0][1]
res = bricks[0][1]

for i in range(1, n):
    max_h = 0
    
    for j in range(i - 1, -1, -1):
        if bricks[j][2] > bricks[i][2] and dy[j] > max_h:
            max_h = dy[j]
    
    dy[i] = max_h + bricks[i][1]        # if문에서 만족하는 벽돌을 못 찾았으면 max_h가 0인데 이는 결국 자기 자신인 bricks[i]만 올릴 수 밖에 없다는 뜻이 된다.
    res = max(res, dy[i])

# print(dy)
print(res)