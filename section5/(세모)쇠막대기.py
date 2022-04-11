import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

bracket = list(input().rstrip())
sum = 0
cnt = 0
for i in range(0, len(bracket)):
    if bracket[i] == '(':
        cnt += 1
    elif bracket[i] == ')' and bracket[i - 1] == '(':
        cnt -= 1
        sum += cnt
    else:
        cnt -= 1
        sum += 1

print(sum)

# stack 이용
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# s = input().rstrip()
# stack = []
# cnt = 0

# for i in range(len(s)):
#     if s[i] == '(':
#         stack.append(s[i])
#     else:
#         stack.pop()
#         if s[i - 1] == '(':
#             cnt += len(stack)
#         else:
#             cnt += 1

# print(cnt)