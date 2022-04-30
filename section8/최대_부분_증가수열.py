# 들러붙을 수 있다면 가장 길이가 긴 증가수열에 붙는 것이 좋다.
# 마지막에 해당 숫자가 오게되면 얼마나 긴 증가수열을 만들 수 있는지 생각하면 된다.
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.insert(0, 0)
d = [0] * (n + 1)
d[1] = 1
res = 0

for i in range(2, n + 1):
    max = 0
    
    for j in range(i - 1, 0, -1):
        if data[j] < data[i] and d[j] > max:       # data[i] 앞에 있는 숫자들
            max = d[j]
            
    d[i] = max + 1
    
    if d[i] > res:
        res = d[i]
        
print(res)
print(d)            
