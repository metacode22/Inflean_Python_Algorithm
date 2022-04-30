import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

#     상  우  하  좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 , -1]
board = [list(map(int, input().split())) for _ in range(7)]     # 내가 갈 수 있는지 없는지 나타내주는 지표
dis = [[0] * 7 for _ in range(7)]   # 실제로 내가 지나가는 길들

queue = deque()
queue.append((0, 0))
board[0][0] = 1                     # 처음 시작점이니 다시 방문하면 안되므로 1로 설정

while queue:
    tmp = queue.popleft()           # 처음엔 (0, 0)이 나올 것이다. 그리고 트리를 생각했을 때 왼쪽부터 순서대로 나올거임.
    for i in range(4):              # 1개가 popleft되면, 즉 1개가 나오면 무조건 4방향 탐색을 해줘야 한다.
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0:     # 좌표 밖으로 나가면 안되고 board에서 0으로 찍혀져 있어야 갈 수 있는 길이다.
            board[x][y] = 1          # 다시 못 가도록 벽으로 만든다.
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1     # 실제로 지나가는 곳들. 이전의 것으로부터 +1을 하므로 계속해서 더해진다.
            queue.append((x, y))     # queue로 while문이 돌 동안 다음 시작점을 가르쳐줌.

if dis[6][6] == 0:                   # 탐색을 다 마쳤는데도 0이 되어 있으면 가는 방법을 찾지 못한 것이다.
    print(-1)
else:
    print(dis[6][6])                 # 가장 '먼저' 닿은 것이 dis[6][6]을 0에서 다른 숫자로 바꿔놓을 것이다. 
                                     # 그리고 board에 해당하는 자리를 1로 만들기 때문에 다른 것이 닿아도 숫자를 바꿀 수 없다.(if문에서 board가 1이라서 걸러진다.)
        