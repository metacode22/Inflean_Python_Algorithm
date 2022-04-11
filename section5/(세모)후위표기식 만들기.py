import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a = input().rstrip()
stack = []
res = ''
for x in a:
    if x.isdecimal():
        res += x
    else:
        if x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == '(':
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()

while len(stack) != 0:
    res += stack.pop()

print(res)
