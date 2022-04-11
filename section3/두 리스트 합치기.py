import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
a1 = list(map(int, input().split()))
m = int(input())
a2 = list(map(int, input().split()))

arr = []

p1 = 0
p2 = 0

while p1 < len(a1) and p2 < len(a2):
    if a1[p1] <= a2[p2]:
        arr.append(a1[p1])
        p1 += 1
    else:
        arr.append(a2[p2])
        p2 += 1

if p1 < len(a1):
    for i in range(p1, len(a1)):
        arr.append(a2[i])
if p2 < len(a2):
    for j in range(p2, len(a2)):
        arr.append(a2[j])

print(*arr)