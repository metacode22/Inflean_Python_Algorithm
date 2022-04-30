# 재귀는 자기 자신을 불러들이는 것.
# for문을 대체할 수 있다. 즉 반복을 효과적으로 할 수 있는게 재귀이다.
# 3중, 4중 for문을 하기에는 효율성이 떨어지는 것들이 있다.
# 이를 재귀로 처리하면 효율적이다.

# 재귀함수는 스택을 이용해서 작동된다.
# 스택이라는 메모리에 기록을 하면서 작동한다.

import sys
input = sys.stdin.readline

n = int(input())

# def DFS(x):
#     if x > 0:
#         print(x)
#         DFS(x - 1)

# DFS(n)

def DFS(x):
    if x > 0:
        DFS(x - 1)
        print(x)

DFS(n)