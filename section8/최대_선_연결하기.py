# 길이가 최대가 되는, 오름차순의 최대 증가수열을 찾으면 된다.
# 오름차순이 아니라면 교차될 수 있고 이는 최대로 선을 그을 수 없음을 의미한다.
# 다음 것이 커지는 순간 선을 더 그을 수 있게 된다.
# 선을 많이 그으려면 길이가 최대가 되는, 오름차순의 최대 부분 증가수열을 찾아야 한다.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.insert(0, 0)
dy = [0] * (n + 1)
dy[1] = 1
res = 0
for i in range(2, n + 1):
    max = 0
    
    for j in range(i - 1, 0, -1):
        if data[i] > data[j] and dy[j] > max:
            max = dy[j]
            
    dy[i] = max + 1 
    
    if dy[i] > res:
        res = dy[i]
        
print(res)
    
