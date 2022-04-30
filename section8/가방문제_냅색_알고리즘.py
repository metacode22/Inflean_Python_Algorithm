import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
data = list()
for _ in range(n):
    data.append(list(map(int, input().split())))
dp = [0] * (m + 1)

for w, v in data:
    for i in range(1, m + 1):
        if i - w >= 0:
            dp[i] = max(dp[i], dp[i - w] + v)
            
print(dp[-1])