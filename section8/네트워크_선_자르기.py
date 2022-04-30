# Bottom-Up 방식, 진짜 동적 계획법(다이나믹 프로그래밍)은 Bottom-Up 방식이다.
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n = int(input())
# d = [0] * (n + 1)
# d[1] = 1
# d[2] = 2

# for i in range(3, n + 1):
#     d[i] = d[i - 1] + d[i - 2]
    
# print(d[n])



# Top-Down 방식(재귀, 메모이제이션)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
d = [0] * (n + 1)

def DFS(len):
    if d[len] > 0:      # 테이블에서 이미 바뀌어져 있다면 가지치기를 하지 말고 테이블의 값을 그대로 리턴하라는 뜻이다.
        return d[len]
    
    if len == 1 or len == 2:
        return len
        
    else:
        d[len] = DFS(len - 1) + DFS(len - 2)
        return d[len]
    
DFS(n)
print(d[n])