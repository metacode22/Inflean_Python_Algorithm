import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(input().rstrip())
cnt = 0
stack = []

for i in range(n):
    while stack and cnt < k and stack[-1] < num[i]:
        stack.pop()
        cnt -= 1
    stack.append(num[i])

