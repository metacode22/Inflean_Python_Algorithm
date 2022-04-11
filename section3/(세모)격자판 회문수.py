import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(3):
    for j in range(7):
        tmp = a[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1

        for k in range(5//2):
            if a[i + k][j] != a[i + 4 - k][j]:
                break
        else:
            cnt += 1

print(cnt)
