# 조합은 기존의 level 말고도 다른 인수(start)가 필요하다.
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
res = [0] * (n + 1)
cnt = 0

def DFS(level, start):
    global cnt
    
    if level == m:
        for j in range(m):              # 그저 res를 출력하기 위한 공간일 뿐이다.
            print(res[j], end = ' ')
        cnt += 1
        print(res)
        print()

    else:
        for i in range(start, n + 1):   # 재귀를 거칠 수록 start가 올라가고 for문의 시작점이 높아지는 동시에 for문의 범위가 줄어든다.
            res[level] = i              # 이렇게 가닥을 뻗을 때 res에 저장되고 재귀에 들어간다.
            DFS(level + 1, i + 1)       # start + 1이 아니라 i + 1이다. 주의 필요.

DFS(0, 1)
print(cnt)
