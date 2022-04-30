# <나의 풀이>
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n = int(input())
# coin = list(map(int, input().split()))
# cost = int(input())
# a = list()
# def DFS(level, sum):
#     if sum >= cost:
#         a.append(level)
#         return
        
#     else:
#         for i in range(n):
#             DFS(level + 1, sum + coin[i])
#     pass

# DFS(0, 0)
# print(min(a))



# <강의 풀이>
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
coin = list(map(int, input().split()))
coin.sort(reverse=True)     # coin을 sort해주지 않으면 처음에 1 1 1 1 1 1 1 1 1 들어가면서 원하는 답에 도착하는 데에 오래 걸릴 수 있다.
cost = int(input())         # 내림차순으로 sort해주어 5 5 5로 들어가게 되면 처음에 빠르게 답을 찾을 수 있다.
res = float('inf')

def DFS(level, sum):        # level이 동전을 사용한 갯수이다. 동전의 갯수
    global res
    if level > res:         # 만약 우리가 처음에 level 3을 찾았고, res로 저장해뒀다면,
        return              # 이후 level 4에 대한 재귀들은 할 필요가 없다. 어차피 답이 되지 않으니까.
    
    if sum > cost:
        return
    
    if sum == cost:
        if level < res:
            res = level
    
    else:
        for i in range(n):
            DFS(level + 1, sum + coin[i])

DFS(0, 0)
print(res)