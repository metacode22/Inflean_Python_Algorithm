import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

largest = -2147000000

for i in range(n):
    row_sum = col_sum = 0
    for j in range(n):
        row_sum += arr[i][j]
        col_sum += arr[j][i]
    if row_sum > largest:
        largest = row_sum
    if col_sum > largest:
        largest = col_sum

sum1 = sum2 = 0
for k in range(n):
    sum1 += arr[k][k]
    sum2 += arr[k][n - k - 1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)