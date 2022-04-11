import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

# def digit_num(x):
#     sum = 0
#     for i in str(x):
#         sum += int(i)
#     return sum

max = -2147000000
for x in arr:
    tot = digit_sum(x)

    if tot > max:
        max = tot
        res = x

print(res)